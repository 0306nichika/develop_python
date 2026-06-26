#userCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
# model.pyで定義したカスタムUserモデルをインポート
from .models import customUser
from django.core.exceptions import ValidationError
import re

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
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^[a-zA-Z0-9@.+\-_]+$', username):
            raise ValidationError(
                'この項目は半角英数字と @/./+/-/_ のみ入力できます'
            )
        return username
