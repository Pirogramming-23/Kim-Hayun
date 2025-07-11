from django.urls import path
from reviews.views import * 


urlpatterns = [
    path('', review_list, name='review_list'),
    path('create/', review_create, name='review_create'),  
    path('<int:pk>',review_detail, name='review_detail'),
]