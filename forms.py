from django import forms

from app.modules.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ('author', 'title', 'content')

        widgets = {
            'title'  : forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control editable medium-editor-textarea', 'rows': 10}),
        }
