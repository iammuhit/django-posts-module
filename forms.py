from django import forms

from app.modules.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ('author', 'category', 'title', 'summary', 'content')

        widgets = {
            'author'  : forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title'   : forms.TextInput(attrs={'class': 'form-control'}),
            'summary' : forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'content' : forms.Textarea(attrs={'class': 'form-control editable medium-editor-textarea', 'rows': 10}),
        }
