from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie

# Create your views here.

def review_list(request):
  movies=Movie.objects.all()
  context={"movies":movies}
  
  return render(request,"review_list.html",context)

def review_detail(request, pk):
    # 404 발생 추가함
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        "movie": movie,
    }
    return render(request, "review_detail.html", context)
def review_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        stars = request.POST.get('stars')
        runtime = request.POST.get('runtime')
        review = request.POST.get('review')
        director = request.POST.get('director')
        actors = request.POST.get('actors')
        
        Movie.objects.create(
            title=title,
            year=year,
            genre=genre,
            stars=stars,
            runtime=runtime,
            review=review,
            director=director,
            actors=actors,
        )
        
        return redirect('review_list')

    return render(request, "review_create.html")