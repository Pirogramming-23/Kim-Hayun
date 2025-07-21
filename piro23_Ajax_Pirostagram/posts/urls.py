from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    path('create/', views.post_create, name='post_create'),
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/comment/', views.create_comment, name='create_comment'),
]