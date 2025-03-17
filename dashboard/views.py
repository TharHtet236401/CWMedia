from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Blog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    try:
        blogs = Blog.objects.all().order_by('-created_at')
        if request.headers.get('HX-Request'):
            return render(request, 'dashboard/dashboard_blogs.html', {'blogs': blogs})
        return render(request, 'dashboard/dashboard.html', {'blogs': blogs})
    except Exception as e:
        messages.error(request, 'Error fetching blogs')
        return render(request, 'dashboard/dashboard.html', {'blogs': []})

@login_required
def add_blog(request):
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            form.instance.author = request.user
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid form submission')
                return render(request, 'dashboard/add_blog.html', {'form': form})
        else:
            form = BlogForm()
        return render(request, 'dashboard/add_blog.html', {'form': form})
    except Exception as e:
        messages.error(request, f"Error adding blog: {str(e)}")
        return render(request, 'dashboard/dashboard_blogs.html', {'blogs': Blog.objects.all().order_by('-created_at')})

@login_required
def delete_blog(request, blog_id):
    try:    
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        return redirect('dashboard')
    except Exception as e:
        messages.error(request, 'Error deleting blog')
        return redirect('dashboard')

@login_required
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

def log_out(request):
    logout(request)
    return redirect('log_in')


def log_in(request):
    try:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, 'dashboard/log_in.html', {'form': form})
        
        form = AuthenticationForm()
        return render(request, 'dashboard/log_in.html', {'form': form})
    except Exception as e:
        messages.error(request, f'Login error: {str(e)}')
        return render(request, 'dashboard/log_in.html', {'form': AuthenticationForm()})

def register(request):
    print("it reached here")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(name, email, password)
            user.save()
            print("form saved ahd user created")
            return redirect('log_in')
        else:
            messages.error(request, 'Invalid form submission')
            return render(request, 'dashboard/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
    return render(request, 'dashboard/register.html', {'form': form})
