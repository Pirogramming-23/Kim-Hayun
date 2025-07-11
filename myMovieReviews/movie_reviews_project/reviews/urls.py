from django.urls import path
from reviews.views import * 


urlpatterns = [
  path("",review_list)
]