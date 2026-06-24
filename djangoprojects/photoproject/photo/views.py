from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import PhotoPostForm

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from .models import PhotoPost
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import random

# Create your views here.
class IndexView(ListView):
    '''トップページビュー
    '''
    template_name = 'index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')


@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    '''写真投稿ページのビュー

    PhotoPostFormで定義されているモデルとフィールドと連携して投稿データベースに登録する

    Attributes:
        form_class:モデルとフィールドが登録されたフォームクラス
        template_name:レンダリングするテンプレート
        success_url:  データベースへの登録完了後のリダイレクト先
    '''

    form_class = PhotoPostForm
    model = PhotoPost 
    template_name = "post_photo.html"

    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う

        parameters:
            form(django.forms.Form):
                form_classに格納されているPhotoPostFormオブジェクト
        Return:
            HttpResponseRedirectオブジェクト
                スーパークラスのform_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        '''
        postdata = form.save(commit = False)

        postdata.user = self.request.user

        postdata.save()

        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name='post_success.html'



FILE = "data/likes.json"

@csrf_exempt
def like(request):
    if request.method == "POST":
        data = json.loads(request.body)

        post_id = data["postId"]
        user_id = data["userId"]

        try:
            with open(FILE) as f:
                likes = json.load(f)
        except:
            likes = {}

        if post_id not in likes:
            likes[post_id] = []
            
        # 10%の確率で失敗
        if random.random() < 0.1:
            return JsonResponse({
                "likeCount": len(likes[post_id]),
                "status": "fail"
            })


        if user_id in likes[post_id]:
            likes[post_id].remove(user_id)
        else:
            likes[post_id].append(user_id)

        with open(FILE, "w") as f:
            json.dump(likes, f)

        return JsonResponse({
            "likeCount": len(likes[post_id])
        })
