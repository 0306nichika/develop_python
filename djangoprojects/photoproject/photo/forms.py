# from django.forms import ModelForm
# from .models import PhotoPost

# class PhotoPostForm(ModelForm):
#     '''ModelFormのサブクラス
#     '''
#     class Meta:
#         ''' ModelFormのインナークラス

#         Attributes:
#             model: モデルクラス
#             fields: フォームで使用するモデルのフィールドを設定
#         '''
#         model = PhotoPost
#         fields = ['category', 'title', 'comment', 'image1', 'image2']
from django.forms import ModelForm
from .models import PhotoPost
from django.core.exceptions import ValidationError  

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']

    #  image1の拡張子チェックを追加
    def clean_image1(self):
        image = self.cleaned_data.get('image1')

        if image:
            ext = image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise ValidationError('画像は jpg / jpeg / png のみ対応しています')

        return image

    #  image2の拡張子チェックを追加
    def clean_image2(self):
        image = self.cleaned_data.get('image2')

        if image:
            ext = image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise ValidationError('画像は jpg / jpeg / png のみ対応しています')

        return image
    