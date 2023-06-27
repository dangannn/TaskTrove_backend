from django import forms

from info.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
