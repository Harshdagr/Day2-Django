from django import forms
from.models import *

# from myApp.models import Post


# class Post_form(forms.Form):
#     title=forms.CharField(max_length=20)
#     message = forms.CharField(widget=forms.Textarea)

class Post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
 
# def __str__(self):
#     return self.title

