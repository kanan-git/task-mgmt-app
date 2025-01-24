from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

# GUIDE AS MULTI-LINE STRING
"""
    // Application, komandalara tapşırıqların idarə edilməsində kömək edəcəkdir. //

    #===== ƏsasFunksionallıqlar =====#
    1. İstifadəçi və komanda idarəetməsi.
    2. Taskların yaradılması, yenilənməsi və tamamlanması.
    3. Tapşırıq üçün prioritetlərin təyin edilməsi.
    4. Task tarixçəsinin saxlanması.
    5. Statistik hesabatların yaradılması.

    #===== Texniki Tələblər =====#
    - Backend: Django, Django Rest Framework.
    - Verilənlər Bazası: PostgreSQL.
    - API: Task idarəetməsi üçün endpointlər.

    #===== Deadline =====#
    - February 5, 2025 (III)
"""


# contains active user's tasks
def tasks_list(request):
    count_of_tasks = Task.objects.count()

    if count_of_tasks == 0:
        tasks = False # or empty list
    else:
        tasks = Task.objects.all()

    context = {
        'user': 'id_001', # id_001 guest

        'sort': 'descending', # ascending descending
        'view_mode': 'grid_cards', # grid_cards list_cards

        'current_language': 'en', # en az tr ru

        'tasks': tasks,
        'count': count_of_tasks,

        'is_nav': True, # True False
    }

    if context['user'] == 'guest':
        print('login first')
        return render(request, 'accounts/sign_in.html')
    elif context['user'] == 'id_001':
        print('welcome "user 001"')
        return render(request, 'tasks/tasks_list.html', context)


# user will see him/her statistic information
def dashboard(request):
    context = {
        'user': 'guest',

        'untitled_data': 'empty',

        'is_nav': True,
    }
    return render(request, 'tasks/dashboard.html', context)


# log history of tasks, their status and event information
def log(request):
    context = {
        'user': 'guest',

        'untitled_data': 'empty',

        'is_nav': True,
    }
    return render(request, 'tasks/log.html', context)


# Crud operation, create new task
@login_required
def create_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            task_form.save()

            return redirect('tasks_list')
    else:
        task_form = TaskForm()

        context = {
            'user': 'guest',

            'untitled_data': 'empty',

            'is_nav': True,

            'task_form': task_form,
        }

        return render(request, 'tasks/create_task.html', context)


# crUd operation, update selected task
@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)

        if task_form.is_valid():
            task_form.save()

            return redirect('tasks_list')
    else:
        task_form = TaskForm(instance=task)
        
        context = {
            'user': 'guest',

            'untitled_data': 'empty',

            'is_nav': True,

            'task_form': task_form,

            'active_card': task,
        }
        
    return render(request, 'tasks/update_task.html', context)


# cruD operation, delete selected task
@login_required
def delete_task(request, pk):
    selected_task = Task.objects.get(id=pk)
    selected_task.delete()
    messages.success(request, f'Task ID:{pk} successfully removed.')
    return redirect('tasks_list')


# opening the about page
def about(request):
    context = {
        'user': 'guest',

        'untitled_data': 'empty',

        'is_nav': True,
    }
    return render(request, 'tasks/about.html', context)


# opening the contact page
def contact(request):
    context = {
        'user': 'guest',

        'untitled_data': 'empty',

        'is_nav': True,
    }
    return render(request, 'tasks/contact.html', context)
