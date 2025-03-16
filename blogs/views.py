from django.shortcuts import render
from django.conf import settings
import os
from .models import Blog
from django.contrib import messages
# Create your views here.
def home(request):
    try:
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }
        messages.success(request, "Blogs fetched successfully")
        return render(request, 'blogs/home.html', context)
    except Exception as e:
        messages.error(request, f"Error: {e}")
        return redirect('home')

def single_blog_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blogs/single_blog.html', context)

