from django.shortcuts import render, redirect, get_object_or_404
from .models import DevTool
from .forms import DevToolForm

# 목록
def devtool_list(request):
    devtools = DevTool.objects.all()
    context = {'devtools': devtools}
    return render(request, 'devtools/devtool_list.html', context)

# create
def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('devtools:devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm()
    context = {'form': form}
    return render(request, 'devtools/devtool_form.html', context)

# detail read
def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    context = {'devtool': devtool}
    return render(request, 'devtools/devtool_detail.html', context)

# update
def devtool_update(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('devtools:devtool_detail', pk=devtool.pk)
    else:
        form = DevToolForm(instance=devtool)
    context = {'form': form, 'devtool': devtool}
    return render(request, 'devtools/devtool_form.html', context)

# delete
def devtool_delete(request, pk):
    devtool = get_object_or_404(DevTool, pk=pk)
    devtool.delete()
    return redirect('devtools:devtool_list')