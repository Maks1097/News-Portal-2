from django import forms
from .models import New

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = [
            'name',
            'description',
            'news',
            'category',
            'categoryType'
        ]


class ArticleForm(NewForm):
    categoryType = forms.ChoiceField(choices=New.CATEGORY_CHOICE, initial='AR', widget=forms.HiddenInput())