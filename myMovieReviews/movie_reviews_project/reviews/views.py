from django.shortcuts import render
from .models import Movie

# Create your views here.

def review_list(request):
  movies=Movie.objects.all()
  context={"movies":movies}
  
  return render(request,"review_list.html",context)