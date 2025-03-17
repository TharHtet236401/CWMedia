from django.shortcuts import render, get_object_or_404
from django.conf import settings
import os
from .models import Blog
from django.contrib import messages
# Create your views here.
def home(request):
    try:
        blogs = Blog.objects.all().order_by('-created_at')
        categories = Blog.CATEGORY_CHOICES
        context = {
            'blogs': blogs,
            'categories': categories
        }
        if request.headers.get('HX-Request'):
            return render(request, 'partials/blogs.html', context)
        # messages.success(request, "Blogs fetched successfully")
        return render(request, 'blogs/home.html', context)
    except Exception as e:
        messages.error(request, f"Error loading blogs: {str(e)}")
        return render(request, 'blogs/home.html', {'blogs': []})

def detailed_blog_view(request, pk):
    try:
        
        blog = get_object_or_404(Blog, pk=pk)
        context = {
            'blog': blog
        }
        return render(request, 'partials/detailed_blog.html', context)
    except Exception as e:
        messages.error(request, f"Error loading blog: {str(e)}")
        return render(request, 'blogs/home.html')

