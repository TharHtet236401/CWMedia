from django import forms    
from blogs.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User;
        fields = ['username', 'password1', 'password2']
        