from django.urls import path
from . import views
from .views import like
from django.views.generic import DeleteView


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
    path('user-list/<int:user>',views.UserView.as_view(),name = 'user_list'),
    path('like/', views.like, name='like'),
    path('photo/<int:pk>/delete',views.PhotoDeleteView(),name = 'photo_delete'),

]