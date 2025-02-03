# IMPORT BUILT-IN LIBRARIES
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

# INSTALLED LIBRARIES
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# IMPORT CUSTOM MODEL & FUNCTIONS
from .models import Task, LogHistory
from .forms import TaskForm
from accounts.models import Profile
from accounts.forms import AccountForm
from .serializers import TaskSerializer


# save all events as user's log history
def log_history(profile, type, message):
    LogHistory.objects.create(user=profile, category=type, event=message)


# HOMEPAGE
def tasks_list(request):
    # COUNTING EXIST ELEMENTS INSIDE DATABASE
    if request.user.is_authenticated:
        count_of_tasks = User.objects.get(id=request.user.id).tasks.all().count()
    else:
        count_of_tasks = 0

    # GET URL PARAMETERS OR DEFAULT
    view_mode = request.GET.get('view') or 'grid'
    current_language = request.GET.get('lang') or 'english'
    sorting_direction = request.GET.get('direction') or 'ascending'
    sorting_type = request.GET.get('sortby') or 'updated_time'
    # searched_string = request.GET.get('search')
    # filter_elements_mark_q = request.GET.get('filter_elements_???')

    # COUNTING HOW MANY PAGE WILL BE THERE
    last_page = count_of_tasks // 9
    pages = []
    if count_of_tasks % 9 > 0:
        last_page += 1
    for index in range(1, last_page+1):
            pages.append(index)

    # GET USER'S TASKS
    if count_of_tasks == 0:
        tasks = False
        last_page = 1
        pages = [1]
        tasks_of_page = []
    else:
        #===== .order_by(type) - both by parameters, add when active | all tries is for considering a possible scenario, which user can change filter or search or other parameter after called task by static request, so that two or more parameter wont work together or directly will raise an error =====#

        if sorting_direction == 'ascending':
                tasks = User.objects.get(id=request.user.id).tasks.all().order_by(sorting_type)
        elif sorting_direction == 'descending':
            tasks = User.objects.get(id=request.user.id).tasks.all().order_by(sorting_type).reverse()

        if request.GET.get('page'):
            page_number = int(request.GET.get('page'))
            first_index_of_the_page = (page_number-1)*9
            final_index_of_the_page = 9*page_number-1
            if final_index_of_the_page >= count_of_tasks:
                final_index_of_the_page = count_of_tasks-1
            tasks_of_page = []

            for i in range(first_index_of_the_page, final_index_of_the_page+1):
                tasks_of_page.append(tasks[i])
        else:
            page_number = 1
            first_index_of_the_page = 0
            final_index_of_the_page = 8
            if final_index_of_the_page >= count_of_tasks:
                final_index_of_the_page = count_of_tasks-1
            tasks_of_page = []

            for i in range(first_index_of_the_page, final_index_of_the_page+1):
                tasks_of_page.append(tasks[i])
        

    # AUTHENTICATED OR GUEST
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

        # 'tasks': tasks,
        'tasks': tasks_of_page,
        'pages': pages,
        'count': count_of_tasks,

        'is_nav': True, # True False
    }

    # OUTPUT
    if auth_stat == False:
        return redirect('sign_in')
    elif auth_stat == True:
        # messages.info(request, f'welcome {nickname}')
        return render(request, 'tasks/tasks_list.html', context)


# user will see him/her statistic information
def dashboard(request):
    auth_stat = request.user.is_authenticated

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=Profile())
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AccountForm(instance=Profile())
    
    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'untitled_data': 'empty',

        'form': form,

        'is_nav': True,
    }

    return render(request, 'tasks/dashboard.html', context)


# log history of tasks, their status and event information
def log(request):
    auth_stat = request.user.is_authenticated
    log_of_user = LogHistory.objects.filter(user=request.user).order_by('-datentime')

    if request.user.is_authenticated:
        nickname = f'{request.user.first_name} {request.user.last_name}'
    else:
        nickname = 'Guest'

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'log': log_of_user,

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
            form = task_form.save(commit=False)
            form.assigned_to = request.user
            form.save()
            # message = messages.success(request, f'New task {task_form.save().id} successfully created.')
            log_history(request.user, 'create', f'New task {task_form.save().id} successfully created.')
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
            log_history(request.user, 'update', f'Task #{task_form.save().id} successfully updated.')
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
    log_history(request.user, 'delete', f'Task #{pk} permanently deleted.')
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


# class based view for Django Rest API
class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        result = Task.objects.all()
        serializers = TaskSerializer(result, many=True)
        return Response(
            {
                'status': 'success', 
                'data': serializers.data
            }, 
            status = 200
        )
    def post(self, request):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': 'success', 
                    'data': serializer.data
                }, 
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'status': 'error', 
                    'data': serializer.errors
                }, 
                status = status.HTTP_400_BAD_REQUEST
            )
