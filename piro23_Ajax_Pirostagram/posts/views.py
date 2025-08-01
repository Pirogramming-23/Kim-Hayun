import json
from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

@login_required 
@require_POST  
def toggle_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    if post.likes.filter(pk=user.pk).exists():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    response_data = {
        'liked': liked,
        'like_count': post.like_count,
    }
    return JsonResponse(response_data)
  
def post_list(request):
	posts = Post.objects.all().order_by('-pk')
	context={
		'posts' : posts,
	}
	return render(request,'posts/post_list.html', context)

@login_required 
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_list')

    else:
        form = PostForm()
    
    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:post_list')
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)

@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    data = json.loads(request.body)
    content = data.get('content')

    if not content:
        return JsonResponse({'status': 'error', 'message': '댓글 내용이 없습니다.'}, status=400)

    comment = Comment.objects.create(
        post=post,
        author=request.user,
        content=content
    )

    return JsonResponse({
        'status': 'ok',
        'comment': {
            'id': comment.id,
            'author': comment.author.username,
            'content': comment.content,
        }
    })
    
@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        return JsonResponse({'status': 'error', 'message': '삭제 권한이 없습니다.'}, status=403)
    
    comment.delete()
    return JsonResponse({'status': 'ok'})