#userCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# model.pyで定義したカスタムUserモデルをインポート
from .models import customUser

class customUserCreationForm(UserCreationForm):
    '''UserCreationFormのサブクラス
    '''
    class Meta:
        '''UserCreationFormのインナークラス
        Attributes:
            model:連携するUserモデル
            fields:フォームで使用するフィールド
        '''

        #連携するuserモデルを設定
        model = customUser
        #フォームで使用するフィールドを設定
        # ユーザー名、メールアドレス、パスワード、パスワード（確認用）
        fields = ('username', 'email', 'password1', 'password2')