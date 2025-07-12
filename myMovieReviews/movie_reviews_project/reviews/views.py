from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie

# Create your views here.

def review_list(request):
  movies=Movie.objects.all()
  context={"movies":movies}
  
  return render(request,"review_list.html",context)

def review_detail(request, pk):
    # 404로 가져오기로 바꿈
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

def review_update(request,pk):
  movie = get_object_or_404(Movie, pk=pk)
  
  if request.method=='POST':
    movie.title = request.POST.get('title')
    movie.year = request.POST.get('year')
    movie.genre = request.POST.get('genre')
    movie.stars = request.POST.get('stars')
    movie.runtime = request.POST.get('runtime')
    movie.review = request.POST.get('review')
    movie.director = request.POST.get('director')
    movie.actors = request.POST.get('actors')
    movie.save()
    return redirect('review_detail', pk=movie.pk)
  #수정 버튼 눌렀을떄 기존 화면 보여주기 구현
  else:
    context = {
            'movie': movie,
        }
    
    return render(request, 'review_form.html', context)

def review_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        movie.delete() 
        return redirect('review_list')
    
    return redirect('review_detail', pk=movie.pk)