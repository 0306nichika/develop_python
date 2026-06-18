from django.urls import path
from . import views

#URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

#URLパターンを登録する変数
urlpatterns = [
    # PhotoアプリへのアクセスはviewモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name = 'index'),
]