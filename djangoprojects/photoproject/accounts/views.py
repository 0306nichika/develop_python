from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import customUserCreationForm
from django.urls import reverse_lazy
 
class SignUpView(CreateView):
    '''サインアップのビュー
 
    '''
    from_class = customUserCreationForm
    template_name ="signup.html"
    success_url = reverse_lazy('accouynts:signup_success')
 
    def from_valid(self, form):
        '''CreateViewクラスのfrom_valid()をオーバーライド
        フォームのバリデーションを通過したときに呼ばれる
        フォームのデータの登録を行う
        parameters:
            from(django.froms.Form):
            from_classに格納されているCustomUserCreationFromオブジェクト
        Return:
            HttpResponseRedirectオブジェクト:
                スーパークラスのfrom_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        '''
        user = form.save()
        self.object = user
        return super().form_valid(form)
class SignUpSuccessView(TemplateView):
    '''サインアップ完了ページのビュー
    '''
 
    template_name = "signup_success.html"
# Create your views here.
