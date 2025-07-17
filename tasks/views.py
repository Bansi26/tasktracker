from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            due_date=request.POST['due_date'],
            status=request.POST['status']
        )
        return redirect('dashboard')
    return render(request, 'task_form.html')

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.status = request.POST['status']
        task.save()
        return redirect('dashboard')
    return render(request, 'task_form.html', {'task': task})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('dashboard')
