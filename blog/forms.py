from django import forms

from .models import Comment, SubComment

from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class SubCommentForm(forms.ModelForm):
    class Meta:
        model = SubComment
        fields = ('body',)
