from django.db import models

# Create your models here.
from accounts.models import customUser

class Category(models.Model):
    '''投稿する写真のカテゴリを管理するモデル'''
    #カテゴリ名のフィールド
    title = models.CharField(
            verbose_name= 'カテゴリ',
            max_length=20
    )
    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        Returns(str):カテゴリ名'''
        return self.title
class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル'''
    #customerUserモデル（のuser_id）とPhotoを
    #1対多の関係で結びつける
    #customerUserが親でPhotoPostが子の関係になる
    user = models.ForeignKey(
        customUser,
        #フィールドのタイトル
        verbose_name='ユーザー',
        #ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
    )
    #Categoryモデル（のtitle）とPhotoを
    #1対多の関係で結びつける
    #Categoryが親でPhotoPostが子の関係になる
    category = models.ForeignKey(
        Category,
        #フィールドのタイトル
        verbose_name='カテゴリ',
        #カテゴリに関連付けられた投稿データが存在する場合は
        #そのカテゴリを削除できないようにする
        on_delete=models.PROTECT,
    )
    title = models.CharField(
        #フィールドのタイトル
        verbose_name='タイトル',
        max_length=200
    )
    comment = models.TextField(
        #フィールドのタイトル
        verbose_name='コメント'
    )
    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to='photos'
    )
    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to='photos',
        blank=True,
        null=True
    )
    posted_add = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    def __str__(self):
        '''オブジェクトを文字列にして返す
        '''
        return self.title