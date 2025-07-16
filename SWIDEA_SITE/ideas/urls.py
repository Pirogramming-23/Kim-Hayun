from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    
    path('create/', views.idea_create, name='idea_create'),

    path('<int:pk>/', views.idea_detail, name='idea_detail'),

    path('<int:pk>/update/', views.idea_update, name='idea_update'),

    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    
    path('<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('<int:pk>/adjust_interest/', views.adjust_interest, name='adjust_interest'),
]
