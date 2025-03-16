from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
]

