from django import forms
from bootstrap3.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
