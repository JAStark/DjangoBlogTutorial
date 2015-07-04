from django import forms
from .models import Post

class PostForm(forms.ModelForm):  #  inherit class to make correct type of model
    class Meta:                   #  tell Django which model to yse to create this form (model = Post)
        model = Post
        fields = ('title', 'text',)  #  only these 2 because author will be whoever is logged in. 
