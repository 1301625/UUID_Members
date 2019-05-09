from django.db import models
from django.urls import reverse
# Create your models here.

from django import forms

#썸네일 패키지
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill,Thumbnail,SmartResize,Resize

#제목 글자 검사
#model에 validators 를 정의하는 것을 권장
def min_length_2_validator(value):
    if len(value) <2:
        raise forms.ValidationError('2글자 이상 입력')


class Post(models.Model):
    title = models.CharField(max_length=200, validators=[min_length_2_validator])
    content = models.TextField(blank=True,null=True)
    #photo = models.ImageField(blank=True,null=True,upload_to='post_photo')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    #썸네일
    # photo_thumbnail = ImageSpecField(
    #     source='photo',
    #     processors=[Resize(300,200)],
    #     format='PNG',
    #     options={'quality': 60}
    # )
    #media폴더, 지정된 폴더 이미지 불러오기
    photo = ProcessedImageField(
        blank=True,
        null=True,
        upload_to='post_photo',
        processors=[Resize(500,500)],
        format='PNG',
        options={'quality':60},
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self): #redirect시 활용
        return reverse('blog:post_detail', args=[self.id])