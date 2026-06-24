from django.urls import path
from . import views

#URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

#URLパターンを登録する変数
urlpatterns = [
    # PhotoアプリへのアクセスはviewモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name = 'index'),
    # 写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/',views.CreatePhotoView.as_view(),name='post'),
    path('post_done/',views.PostSuccessView.as_view(),name="post_done"),

    path('photos/<int:category>/',views.CategoryView.as_view(),name = 'photos_映画ポスター'),
]