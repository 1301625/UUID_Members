from django import forms
from .models import Post


#Form 과 Model Form 차이점
#Form 직접 필드 정의 위젯 설정이 필요
#model Form 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'


def min_length_3_validator(value):
    if len(value) <3:
        raise forms.ValidationError('3글자이상 입력해주세요')


class PostForm(forms.Form):
    title=forms.CharField(label="제목")
    #title=forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea,label="내용")
    photo = forms.ImageField()

    #ModelForm.save 인터페이스를 흉내내어 구현
    #ModelForm이 아니면 save구현해야함
    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post

