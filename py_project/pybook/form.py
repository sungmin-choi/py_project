from .models import Book, Comment
from django import forms


class BookCommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['comment_textfield']
        widgets = {
            'comment_textfield': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }
