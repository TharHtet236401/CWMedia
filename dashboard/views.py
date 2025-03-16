from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
# Create your views here.
def dashboard(request):
    try:
        blogs = Blog.objects.all().order_by('-created_at')
        if request.headers.get('HX-Request'):
            return render(request, 'dashboard/dashboard_blogs.html', {'blogs': blogs})
        return render(request, 'dashboard/dashboard.html', {'blogs': blogs})
    except Exception as e:
        messages.error(request, 'Error fetching blogs')
        return render(request, 'dashboard/dashboard.html', {'blogs': []})

def delete_blog(request, blog_id):
    try:    
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        return redirect('dashboard')
    except Exception as e:
        messages.error(request, 'Error deleting blog')
        return redirect('dashboard')

def edit_blog(request, blog_id):
    try:
        blog = get_object_or_404(Blog, pk=blog_id)
        form = BlogForm(instance=blog)
        if request.method == 'POST':
            form = BlogForm(request.POST, instance=blog)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        return render(request, 'dashboard/edit_blog.html', {'form': form, 'blog': blog})
    except Exception as e:
        messages.error(request, f"Error editing blog: {str(e)}")
        return render(request, 'dashboard/dashboard_blogs.html', {'blogs': Blog.objects.all().order_by('-created_at')})
