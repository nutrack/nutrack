from django import forms
from article.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comment_post']
        widgets = {
            'comment_post': forms.Textarea(
                attrs={
                'class': "form-control",
                'style': 'max-width: 700px;',
                'placeholder': 'Say something...'
                }
            )
        }