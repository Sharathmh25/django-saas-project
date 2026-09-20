from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


@login_required
def create_task(request):
    if request.user.tenant is None:
        return redirect('create_tenant')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.tenant = request.user.tenant
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/create.html',{'form':form})


@login_required
def task_list(request):
    if request.user.tenant is None:
        return redirect('create_tenant')
    tasks=Task.objects.filter(tenant=request.user.tenant)
    return render(request, 'task/list.html', {'tasks': tasks})


@login_required
def update_task(request,task_id):
    tasks = get_object_or_404(Task, id=task_id, tenant=request.user.tenant)
    if request.method=='POST':
        form=TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm(instance=tasks)
    return render(request,'task/update.html',{'form':form,'task':tasks})


@login_required
def delete_task(request,task_id):
    if request.method != 'POST':
        return redirect('task_list')
    task = get_object_or_404(Task, id=task_id, tenant=request.user.tenant)
    task.delete()
    return redirect('task_list')