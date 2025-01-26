from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    # COUNTING EXIST ELEMENTS INSIDE DATABASE
    if request.user.is_authenticated:
        # count_of_tasks = Task.objects.count()
        count_of_tasks = User.objects.get(id=request.user.id).tasks.all().count()
    else:
        count_of_tasks = 0

    # DEFAULT PARAMETERS FOR CONTROL BAR
    sorting_direction = 'ascending'
    sorting_type = 'updated_time'
    view_mode = 'grid_cards'
    current_language  = 'en'

    # CHANGING SORT DIRECTION
    if request.POST.get('direction') == 'ascending':
        sorting_direction = 'ascending'
    elif request.POST.get('direction') == 'descending':
        sorting_direction = 'descending'

    # CHANGING SORT TYPE
    if request.POST.get('sort_by') == 'todo':
        sorting_type = 'todo'
    elif request.POST.get('sort_by') == 'priority_level':
        sorting_type = 'priority_level'
    elif request.POST.get('sort_by') == 'added_time':
        sorting_type = 'added_time'
    elif request.POST.get('sort_by') == 'updated_time':
        sorting_type = 'updated_time'

    # GET ALL TASKS IF THERE IS ANY
    if count_of_tasks == 0:
        tasks = False # or empty list
    else:
        # tasks = Task.objects.all()
        if sorting_direction == 'ascending':
            # tasks = Task.objects.all().order_by(sorting_type)
            tasks = User.objects.get(id=request.user.id).tasks.all().order_by(sorting_type)
        elif sorting_direction == 'descending':
            # tasks = Task.objects.all().order_by(sorting_type).reverse()
            tasks = User.objects.get(id=request.user.id).tasks.all().order_by(sorting_type).reverse()

    # HANDLING VIEW MODES OF TASK CARDS
    if request.POST.get('view') == 'list_cards':
        view_mode = 'grid_cards'
    elif request.POST.get('view') == 'grid_cards':
        view_mode = 'list_cards'

    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    # SENDING REQUIRED INFORMATION TO THE HOMEPAGE
    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'sort_direction': sorting_direction,
        'sort_type': sorting_type,
        'view_mode': view_mode,
        'current_language': current_language,

        'tasks': tasks,
        'count': count_of_tasks,

        'is_nav': True, # True False
    }

    # ...
    if auth_stat == False:
        # print('login first')
        return render(request, 'accounts/sign_in.html')
    elif auth_stat == True:
        # print(f'welcome {nickname}')
        # messages.info(request, f'welcome {nickname}')
        return render(request, 'tasks/tasks_list.html', context)


# user will see him/her statistic information
def dashboard(request):
    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'untitled_data': 'empty',

        'is_nav': True,
    }

    return render(request, 'tasks/dashboard.html', context)


# log history of tasks, their status and event information
def log(request):
    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'untitled_data': 'empty',

        'is_nav': True,
    }

    return render(request, 'tasks/log.html', context)


# Crud operation, create new task
@login_required
def create_task(request):
    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    if request.method == 'POST':
        task_form = TaskForm(request.POST)

        if task_form.is_valid():
            task_form.save()

            return redirect('tasks_list')
    else:
        task_form = TaskForm()

        context = {
            'user': nickname,
            'auth_stat': auth_stat,

            'untitled_data': 'empty',

            'is_nav': True,

            'task_form': task_form,
        }

        return render(request, 'tasks/create_task.html', context)


# crUd operation, update selected task
@login_required
def update_task(request, pk):
    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)

        if task_form.is_valid():
            task_form.save()

            return redirect('tasks_list')
    else:
        task_form = TaskForm(instance=task)
        
        context = {
            'user': nickname,
            'auth_stat': auth_stat,

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
    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'untitled_data': 'empty',

        'is_nav': True,
    }
    return render(request, 'tasks/about.html', context)


# opening the contact page
def contact(request):
    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'untitled_data': 'empty',

        'is_nav': True,
    }
    return render(request, 'tasks/contact.html', context)
