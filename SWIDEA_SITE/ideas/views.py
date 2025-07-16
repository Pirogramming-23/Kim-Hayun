from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from django.core.paginator import Paginator
from .models import Idea, IdeaStar
from .forms import IdeaForm

# 아이디어 목록
def idea_list(request):
    sort_by = request.GET.get('sort', 'latest')

    if sort_by == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort_by == 'interest':
        ideas = Idea.objects.all().order_by('-interest', '-pk')
    elif sort_by == 'stars':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count', '-pk')
    else:
        ideas = Idea.objects.all().order_by('-pk')

    paginator = Paginator(ideas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
    }
    return render(request, 'ideas/idea_list.html', context)

@login_required
def toggle_star(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    user = request.user
    
    try:
        star = IdeaStar.objects.get(user=user, idea=idea)
        star.delete()
        is_starred = False
    except IdeaStar.DoesNotExist:
        IdeaStar.objects.create(user=user, idea=idea)
        is_starred = True
        
    star_count = idea.ideastar_set.count()

    return JsonResponse({'is_starred': is_starred, 'star_count': star_count})

@login_required
def adjust_interest(request, pk):
    if request.method == 'POST':
        idea = get_object_or_404(Idea, pk=pk)
        action = request.POST.get('action')

        if action == 'increase':
            idea.interest += 1
        elif action == 'decrease' and idea.interest > 0:
            idea.interest -= 1
        
        idea.save()
        return JsonResponse({'interest': idea.interest})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
# 아이디어 등록
@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.author = request.user # 현재 로그인한 사용자를 작성자로 설정
            idea.save()
            return redirect('ideas:idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    context = {'form': form}
    return render(request, 'ideas/idea_form.html', context)

# 아이디어 읽기
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    is_starred = False
    if request.user.is_authenticated:
        if IdeaStar.objects.filter(user=request.user, idea=idea).exists():
            is_starred = True
            
    context = {
        'idea': idea,
        'is_starred': is_starred,
    }
    return render(request, 'ideas/idea_detail.html', context)

# 아이디어 수정
@login_required
def idea_update(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    # 작성자만 수정 가능
    if request.user != idea.author:
        return redirect('ideas:idea_list')

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    context = {'form': form, 'idea': idea}
    return render(request, 'ideas/idea_form.html', context)

# 아이디어 삭제
@login_required
def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
  
    if request.user == idea.author:
        idea.delete()
    return redirect('ideas:idea_list')