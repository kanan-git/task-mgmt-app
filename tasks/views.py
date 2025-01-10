from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

# GUIDE 1 AS MULTI-LINE STRING
"""
    Application, komandalara tapşırıqların idarə edilməsində kömək edəcəkdir.

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
"""

# GUIDE 2 AS MULTI-LINE STRING
"""
    #===== APPLICATIONS OF PROJECT =====#
    - users
    - tasks
    - music player
    - quotes
    - clock and timer

    #===== PLANNED FEATURES =====#
    - task cards like product cards, with type, category and title
    - categories like home, workout, study, hobby, entertaintment, etc
    - sort by alphabet, priority point, added time, update time
    - filter by done or incomplete or work in progress, category, added time, update time, point, type
    - trigger for remind or schedule tasks, check clock and calendar realtime
    - add music player if possible, even library folder to play from there, with default django player or features, not 3rd party
    - add motivational quotes by category or more fit to selected task itself
    - besides main bootstrap styles, add some custom js and css for some demonstrations if there is time, consider responsiveness
    - authentication
    - crud (create, read, update, delete) functions for handle tasks
    - search system
    - clock and timer for focus mode
    - type of task, beside normal true false cards, make counter card, each click add some point to card to fill it, when you done, it explodes and complete
    - log
    - dashboard, nece priority 10 taskim olub, nece lvl5, nece taski tamamlamisam, nece task yaradilib ve s melumatlar olan profile bolmesi kimi birsey

    #===== MILESTONES AND DEADLINE =====#
    - first day, January 5, 2025, VII
    - milestone 1, January 12, 2025, VII
    - milestone 2, January 19, 2025, VII
    - milestone 3, January 26, 2025, VII
    - milestone 4, February 2, 2025, VII
    - last day, February 5, 2025, III

    #===== GRAPHIC ASSETS =====#
    - custom wallpapers for each category
    - logo which already created
    - prioritiy tier list animated rectangle small images
    - custom renders or ai generator api by custom premade prompts or filter from task
"""


# contains active user's tasks
def tasks_list(request):
    context = {
        'untitled_data': 'empty'
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


# cRud operation, read selected task detailed
def read_task(request, pk):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'tasks/read_task.html', context)


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
