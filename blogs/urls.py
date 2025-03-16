from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.detailed_blog_view, name='detailed_blog_view'),
]

