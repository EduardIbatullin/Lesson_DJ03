from .models import News_post
from django.forms import ModelForm, TextInput, Textarea


class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'author']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите заголовок"
            }),
            "short_description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите краткое описание"
            }),
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введите текст новости"
            }),
            "author": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите имя автора"
            }),
        }