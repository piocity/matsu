from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """A form to add comment."""
    class Meta:
        model = Comment
        fields = ('contents',)

