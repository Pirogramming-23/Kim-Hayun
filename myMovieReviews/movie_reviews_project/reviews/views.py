from django.shortcuts import render,redirect
from .models import Movie

# Create your views here.

def review_list(request):
  movies=Movie.objects.all()
  context={"movies":movies}
  
  return render(request,"review_list.html",context)

def review_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        review = request.POST.get('review')
        return redirect('review_list')

    return render(request, "review_create.html")