from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-post/', views.create_post, name='create-post'),
    path('view-post/<int:pk>/', views.post_view, name='view-post'),
    path('edit-post/<int:pk>/', views.update_post, name='edit-post'),
    path('delete-post/<int:pk>/', views.deletepost, name='delete-post'),
]