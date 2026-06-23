from django.urls import path
# viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views
# URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューを呼び出し
    # [http(s)://<ホスト名>/signup/]へのアクセスに対し
    # viewsモジュールのSignUpViewsをインスタンス化する
    path('signup/',
         views.SignUpView.as_view(),
         name = 'signup',
    ),
    
    #サインアップ完了ページのビューを呼び出し
    # [http(s)://<ホスト名>/signup_success/]へのアクセスに対し
    # viewsモジュールのSignUpSuccessViewsをインスタンス化する
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name = 'signup_success',
    ),

    # ログインページの表示
    # [http(s)://<ホスト名>/signup/]へのアクセスに対し
    # django.contrub.auth.views.LoginViewをインスタンス化して
    # ログインページを表示する
    path('login/',
         # ログイン用テンプレート（フォーム）をレンダリング
         auth_views.LoginView.as_view(template_name='login.html'),
         name = 'login'
         ),
     
     # ログアウトを実行
     # [http(s)://<ホスト名>/logout/]へのアクセスに対して
     # django.contrub.auth.views.LogoutViewをインスタンス化して
     # ログアウトさせる
     path('logout/',
          auth_views.LogoutView.as_view(template_name='logout.html'),
          name = 'logout',
          ),
     
     path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'
         ),

]
