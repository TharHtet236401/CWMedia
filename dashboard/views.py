from django.shortcuts import render, redirect
from blogs.models import Blog
from django.contrib import messages
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
        messages.success(request, 'Blog deleted successfully')
        return redirect('dashboard')
    except Exception as e:
        messages.error(request, 'Error deleting blog')
        return redirect('dashboard')


