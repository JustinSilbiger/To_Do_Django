from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.filter(completed=False)  # Only show tasks that are not completed
    form = TaskForm()

    if request.method == 'POST' and 'title' in request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'polls/index.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'polls/update_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'polls/delete_task.html', context)

def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.completed = True
        task.save()
        return redirect('/')
