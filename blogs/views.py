from django.shortcuts import render
from django.conf import settings
import os
from .models import Blog

# Create your views here.
def home(request):
    # Debug prints
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/home.html', context)

