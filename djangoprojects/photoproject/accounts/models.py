from django.db import models
# AbstractUserクラスをインポート
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    '''
    Userモデルを継承したカスタムユーザーモデル
    '''
    pass


# Create your models here.
