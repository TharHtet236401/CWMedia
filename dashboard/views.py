from django.shortcuts import render
from blogs.models import Blog
# Create your views here.
def dashboard(request):
    blogs = Blog.objects.all()
    return render(request, 'dashboard/dashboard.html', {'blogs': blogs})

