from django.shortcuts import render, redirect
from .models import Task, Comment
from .forms import TaskForm, CommentForm


def index(request):
    tasks = Task.objects.order_by('-id')
    context = {'tasks': tasks}
    return render(request, 'main/index.html', context)


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    comments = Comment.objects.order_by('-id')
    if request.method == 'POST':
        forma = CommentForm(request.POST)
        if forma.is_valid():
            forma.save()

    forma = CommentForm()
    context = {'task': task, 'comments': comments, 'forma': forma}
    return render(request, 'main/task.html', context)


def add(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            error = 'Форма заполнена некорректно'

    form = TaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/add.html', context)
