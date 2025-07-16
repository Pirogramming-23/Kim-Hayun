from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Idea, IdeaStar
from .forms import IdeaForm

# 아이디어 목록
def idea_list(request):
    ideas = Idea.objects.all().order_by('-pk') # 최신순으로 정렬
    context = {'ideas': ideas}
    return render(request, 'ideas/idea_list.html', context)

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