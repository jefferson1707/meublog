from django.urls import path
from . import views

# Namespace para as URLs
app_name = 'blog'

# Definição das URLs
urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),

]

