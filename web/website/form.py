from django import forms
from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('yourname', 'email', 'text_comment')
