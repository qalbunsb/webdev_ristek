from django import forms
from .models import *

class BlogPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Post
        fields = ('title','categories','image','body')
        widgets = {
            'categories' : forms.Select 
        }

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }
    class Meta:
        model = Category
        fields = '__all__'

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs = {
            'class': 'form-control'
        }
    class Meta:
        model = Comment
        fields = ('desc',)
