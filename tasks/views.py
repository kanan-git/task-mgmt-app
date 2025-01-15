from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task, Category
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
    count_of_categories = Category.objects.count()

    if count_of_tasks == 0:
        tasks = False # or empty list
    else:
        tasks = Task.objects.all()

    if count_of_categories == 0:
        list_of_categories = False # or empty list
    else:
        list_of_categories = Category.objects.all()

    context = {
        'user': 'guest',
        'sort': 'descending',
        'view_mode': 'grid_cards',

        'tasks': tasks,
        'count': count_of_tasks,
        'list_of_categories': list_of_categories,
    }

    return render(request, 'tasks/tasks_list.html', context)


# user will see him/her statistic information
def dashboard(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'tasks/dashboard.html', context)


# log history of tasks, their status and event information
def log(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'tasks/log.html', context)


# Crud operation, create new task
def create_task(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'tasks/create_task.html', context)


# crUd operation, update selected task
def update_task(request, pk):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'tasks/update_task.html', context)


# cruD operation, delete selected task
def delete_task(request, pk):
    return redirect('tasks/tasks_list')


# opening the about page
def about(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'tasks/about.html', context)


# opening the contact page
def contact(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'tasks/contact.html', context)
