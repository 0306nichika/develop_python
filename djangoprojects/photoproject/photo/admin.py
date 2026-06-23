from django.contrib import admin

# Register your models here.
from .models import Category, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    list_display = ('id', 'title')

    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    '''
    list_display = ('id', 'title')

    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)

admin.site.register(PhotoPost, PhotoPostAdmin)