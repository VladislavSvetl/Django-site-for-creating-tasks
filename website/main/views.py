from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    context = {'tasks': tasks}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


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
