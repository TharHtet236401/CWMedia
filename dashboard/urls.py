from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]

