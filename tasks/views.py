# IMPORT BUILT-IN LIBRARIES
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime

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
    #===== COUNTING EXIST ELEMENTS INSIDE DATABASE =====#
    if request.user.is_authenticated:
        count_of_tasks = User.objects.get(id=request.user.id).tasks.all().count()
    else:
        count_of_tasks = 0

    #===== GET URL PARAMETERS OR DEFAULT =====#
    view_mode = request.GET.get('view') or 'grid'
    current_language = request.GET.get('lang') or 'english'
    sorting_direction = request.GET.get('direction') or 'ascending'
    sorting_type = request.GET.get('sortby') or 'updated_time'
    searched_string = request.GET.get('search') or ''
    filtStat = request.GET.get('filt_stat') or 'all'
    filtCateg = request.GET.get('filt_categ') or ''
    filtPriority = request.GET.get('filt_priority') or '1,10'
    filtType = request.GET.get('filt_type') or 'all'

    #===== GET USER'S TASKS =====#
    if count_of_tasks == 0:
        tasks = False
        last_page = 1
        pages = [1]
        tasks_of_page = []
    else:
        #===== FILTER BY DIRECTION =====#
        if sorting_direction == 'ascending':
            tasksSrc = User.objects.get(id=request.user.id).tasks.all().order_by(sorting_type)
        elif sorting_direction == 'descending':
            tasksSrc = User.objects.get(id=request.user.id).tasks.all().order_by(sorting_type).reverse()

        #===== FILTER BY TYPE =====#
        if filtType == 'all':
            ic_tasks = []
            wip_tasks = []
            done_tasks = []
            all_of_tasks = []
            tasks = tasksSrc
            for i in range(0, len(tasks)):
                if tasks[i].progression_start > 0 and tasks[i].progression_start < tasks[i].progression_end:
                    wip_tasks.append(tasks[i].id)
                elif tasks[i].progression_start == 0 and tasks[i].progression_start != tasks[i].progression_end:
                    ic_tasks.append(tasks[i].id)
                elif tasks[i].progression_start == tasks[i].progression_end:
                    done_tasks.append(tasks[i].id)
                else:
                    ic_tasks = []
                    wip_tasks = []
                    done_tasks = []
                    try:
                        ...
                    except Exception as Error:
                        print(Error)
                if tasks[i].todo_status == 3:
                    done_tasks.append(tasks[i].id)
            all_of_tasks = ic_tasks + wip_tasks + done_tasks
        elif filtType == 'milestone':
            ic_tasks = []
            wip_tasks = []
            done_tasks = []
            all_of_tasks = []
            tasks = tasksSrc.filter(type_of_task_id=2)
            for i in range(0, len(tasks)):
                if tasks[i].progression_start > 0 and tasks[i].progression_start < tasks[i].progression_end:
                    wip_tasks.append(tasks[i].id)
                elif tasks[i].progression_start == 0 and tasks[i].progression_start != tasks[i].progression_end:
                    ic_tasks.append(tasks[i].id)
                elif tasks[i].progression_start == tasks[i].progression_end:
                    done_tasks.append(tasks[i].id)
                else:
                    ic_tasks = []
                    wip_tasks = []
                    done_tasks = []
                    try:
                        ...
                    except Exception as Error:
                        print(Error)
                if tasks[i].todo_status == 3:
                    done_tasks.append(tasks[i].id)
            all_of_tasks = ic_tasks + wip_tasks + done_tasks
        elif filtType == 'instant':
            ic_tasks = []
            wip_tasks = []
            done_tasks = []
            all_of_tasks = []
            tasks = tasksSrc.filter(type_of_task_id=1)
            for i in range(0, len(tasks)):
                if tasks[i].todo_status == 1:
                    ic_tasks.append(tasks[i].id)
                elif tasks[i].todo_status == 2:
                    wip_tasks.append(tasks[i].id)
                elif tasks[i].todo_status == 3:
                    done_tasks.append(tasks[i].id)
                else:
                    ic_tasks = []
                    wip_tasks = []
                    done_tasks = []
                    try:
                        ...
                    except Exception as Error:
                        print(Error)
                if tasks[i].progression_start == tasks[i].progression_end:
                    done_tasks.append(tasks[i].id)

        #===== FILTER BY CATEGORIES =====#
        listOfCategories = {
            1: 'Personal',
            2: 'Work/PRO',
            3: 'Home',
            4: 'Urgent',
            5: 'Study/School',
            6: 'Health/Sport',
            7: 'Shopping',
            8: 'Finance',
            9: 'Travel',
            10: 'Social/Events',
            11: 'Maintenance',
            12: 'LongTermGoals',
            13: 'Miscellaneous',
            14: 'Team',
            15: 'Creative',
            16: 'Learning/DEV',
            17: 'Family',
            18: 'Technology/IT',
            19: 'Volunteer',
            20: 'Projects',
        }
        filtCategParams = filtCateg.split(',')
        listFilts = []
        for index in range(0, len(filtCategParams)):
            for i in range(1, len(listOfCategories)+1):
                if filtCategParams[index] == listOfCategories[i]:
                    listFilts.append(i)
        #===== FILTER BY STATUS & SEARCH & PRIORITY =====#
        priorityList = filtPriority.split(',')
        priorityMin = int(priorityList[0])
        priorityMax = int(priorityList[1])
        if priorityMin > priorityMax:
            # swap minimum and maximum values
            x = priorityMin
            priorityMin = priorityMax
            priorityMax = x
        if listFilts:
            if filtStat == 'all':
                tasks = tasks.filter(id__in=all_of_tasks, todo__contains=searched_string, category_of_task__in=listFilts, priority_level__gte=priorityMin, priority_level__lte=priorityMax).distinct()
            elif filtStat == 'incomplete':
                tasks = tasks.filter(id__in=ic_tasks, todo__contains=searched_string, category_of_task__in=listFilts, priority_level__gte=priorityMin, priority_level__lte=priorityMax).distinct()
            elif filtStat == 'wip':
                tasks = tasks.filter(id__in=wip_tasks, todo__contains=searched_string, category_of_task__in=listFilts, priority_level__gte=priorityMin, priority_level__lte=priorityMax).distinct()
            elif filtStat == 'done':
                tasks = tasks.filter(id__in=done_tasks, todo__contains=searched_string, category_of_task__in=listFilts, priority_level__gte=priorityMin, priority_level__lte=priorityMax).distinct()
        else:
            if filtStat == 'all':
                tasks = tasks.filter(id__in=all_of_tasks, todo__contains=searched_string, priority_level__gte=priorityMin, priority_level__lte=priorityMax)
            elif filtStat == 'incomplete':
                tasks = tasks.filter(id__in=ic_tasks, todo__contains=searched_string, priority_level__gte=priorityMin, priority_level__lte=priorityMax)
            elif filtStat == 'wip':
                tasks = tasks.filter(id__in=wip_tasks, todo__contains=searched_string, priority_level__gte=priorityMin, priority_level__lte=priorityMax)
            elif filtStat == 'done':
                tasks = tasks.filter(id__in=done_tasks, todo__contains=searched_string, priority_level__gte=priorityMin, priority_level__lte=priorityMax)

        #===== COUNTING HOW MANY PAGE WILL BE THERE =====#
        last_page = len(tasks) // 9
        pages = []
        if len(tasks) % 9 > 0:
            last_page += 1
        for index in range(1, last_page+1):
                pages.append(index)        
        if len(tasks) == 0:
            tasks = False
            last_page = 1
            pages = [1]
            tasks_of_page = []
            count_of_tasks = 0
        else:
            if request.GET.get('page'):
                page_number = int(request.GET.get('page'))
                first_index_of_the_page = (page_number-1)*9
                final_index_of_the_page = 9*page_number-1
                count_of_tasks = len(tasks)
                if final_index_of_the_page >= count_of_tasks:
                    final_index_of_the_page = count_of_tasks-1
                tasks_of_page = []

                for i in range(first_index_of_the_page, final_index_of_the_page+1):
                    tasks_of_page.append(tasks[i])
            else:
                page_number = 1
                first_index_of_the_page = 0
                final_index_of_the_page = 8
                count_of_tasks = len(tasks)
                if final_index_of_the_page >= count_of_tasks:
                    final_index_of_the_page = count_of_tasks-1
                tasks_of_page = []

                for i in range(first_index_of_the_page, final_index_of_the_page+1):
                    tasks_of_page.append(tasks[i])
        
    #===== AUTHENTICATED OR GUEST =====#
    auth_stat = request.user.is_authenticated
    if request.user.is_authenticated:
        if request.user.first_name or request.user.last_name:
            nickname = f'{request.user.first_name} {request.user.last_name}'
        else:
            nickname = 'Anonymous'
    else:
        nickname = 'Guest'

    # CLEAR ALL OF COMPLETED MILESTONE AND INSTANT TASKS
    if request.POST.get('clear_completed'):
        if count_of_tasks:
            if done_tasks:
                for i in done_tasks:
                    for task in tasks:
                        if task.id == i:
                            print(task)
                            log_history(request.user, 'delete', f'Task #{task.id} permanently deleted.')
                            task.delete()
                messages.success(request, 'All completed tasks removed.')
                return redirect('tasks_list')
            else:
                messages.info(request, 'There is no completed task yet.')
        else:
            messages.info(request, 'There is no tasks to clear.')

    #===== SENDING REQUIRED INFORMATION TO THE HOMEPAGE =====#
    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'sort_direction': sorting_direction,
        'sort_type': sorting_type,
        'view_mode': view_mode,
        'current_language': current_language,
        'search': searched_string,
        'filt_stat': filtStat,
        'filt_categ': filtCateg,
        'filt_priority': filtPriority,
        'filt_type': filtType,

        'tasks': tasks_of_page,
        'pages': pages,
        'count': count_of_tasks,

        'is_nav': True, # True False
    }

    #===== OUTPUT =====#
    if auth_stat == False:
        return redirect('sign_in')
    elif auth_stat == True:
        # messages.info(request, f'welcome {nickname}')
        return render(request, 'tasks/tasks_list.html', context)


# user will see him/her statistic information
def dashboard(request):
    # GET URL PARAMETERS OR DEFAULT
    current_language = request.GET.get('lang') or 'english'
    
    """
        • Task completed, for each month at #thisYear: 0 → evvel, log a status elave etmek lazimdir, completed tasklari tanimaq ucun
        • Tasks created at #thisYear: 0
        • Task deleted at #thisYear: 0

        • Max Consecutively Login: 0
        • Max Activity in a Day: 0
        • Total Activity (Auth/Create/Delete): 0
    """

    # TOTAL COUNT OF ELEMENTS
    if request.user.is_authenticated:
        count_of_tasks = User.objects.get(id=request.user.id).tasks.all().count
        count_of_events = LogHistory.objects.filter(user=request.user).count()
    else:
        count_of_tasks = 0
        count_of_events = 0
    
    # RESOURCES
    current_year = datetime.now().year
    tasksSrc = User.objects.get(id=request.user.id).tasks.all()
    tasks = tasksSrc.filter(added_time__month=2, added_time__year=2025)

    # z = tasks[0].added_time
    # print(type(z), z.year)
    # x = str(tasks[0].added_time).split(' ')
    # y = x[0].split('-')
    # print(y)
    # print(datetime.now().year, datetime.now().month)
    # if(z.year == datetime.now().year):
    #     print('working')

    # TASKS WITH PRIORITY LEVEL & STATUS
    priority1TasksCount = 0
    priority2TasksCount = 0
    priority3TasksCount = 0
    priority4TasksCount = 0
    priority5TasksCount = 0
    priority6TasksCount = 0
    priority7TasksCount = 0
    priority8TasksCount = 0
    priority9TasksCount = 0
    priority10TasksCount = 0
    IncompleteTasks = 0
    WIPTasks = 0
    CompletedTasks = 0
    for task in tasksSrc:
        if task.priority_level == 1:
            priority1TasksCount += 1
        elif task.priority_level == 2:
            priority2TasksCount += 1
        elif task.priority_level == 3:
            priority3TasksCount += 1
        elif task.priority_level == 4:
            priority4TasksCount += 1
        elif task.priority_level == 5:
            priority5TasksCount += 1
        elif task.priority_level == 6:
            priority6TasksCount += 1
        elif task.priority_level == 7:
            priority7TasksCount += 1
        elif task.priority_level == 8:
            priority8TasksCount += 1
        elif task.priority_level == 9:
            priority9TasksCount += 1
        elif task.priority_level == 10:
            priority10TasksCount += 1

        if task.todo_status == 1:
            IncompleteTasks += 1
        elif task.todo_status == 2:
            WIPTasks += 1
        elif task.todo_status == 3:
            CompletedTasks += 1
    priorities = {
        'p1': priority1TasksCount,
        'p2': priority2TasksCount,
        'p3': priority3TasksCount,
        'p4': priority4TasksCount,
        'p5': priority5TasksCount,
        'p6': priority6TasksCount,
        'p7': priority7TasksCount,
        'p8': priority8TasksCount,
        'p9': priority9TasksCount,
        'p10': priority10TasksCount
    }
    statusList = {
        'incomplete': IncompleteTasks,
        'wip': WIPTasks,
        'done': CompletedTasks
    }

    # AUTHENTICATED OR GUEST
    auth_stat = request.user.is_authenticated
    if request.user.is_authenticated:
        if request.user.first_name or request.user.last_name:
            nickname = f'{request.user.first_name} {request.user.last_name}'
        else:
            nickname = 'Anonymous'
    else:
        nickname = 'Guest'

    if request.method == 'POST':
        # form = AccountForm(request.POST, instance=Profile())
        # if form.is_valid():
        #     form.save()
        #     return redirect('dashboard')
        ...
    else:
        # form = AccountForm(instance=Profile())
        ...
    
    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'current_language': current_language,

        # 'form': form,

        'priorities': priorities,
        'statusList': statusList,
        'current_year': current_year,

        'is_nav': True,
    }

    return render(request, 'tasks/dashboard.html', context)


# log history of tasks, their status and event information
def log(request):
    # GET URL PARAMETERS OR DEFAULT
    current_language = request.GET.get('lang') or 'english'
    
    # COUNTING EXIST ELEMENTS INSIDE DATABASE
    if request.user.is_authenticated:
        count_of_events = LogHistory.objects.filter(user=request.user).count()
    else:
        count_of_events = 0

    # AUTHENTICATED OR GUEST
    auth_stat = request.user.is_authenticated
    log_of_user = LogHistory.objects.filter(user=request.user).order_by('-datentime')
    if request.user.is_authenticated:
        if request.user.first_name or request.user.last_name:
            nickname = f'{request.user.first_name} {request.user.last_name}'
        else:
            nickname = 'Anonymous'
    else:
        nickname = 'Guest'

    # COUNTING HOW MANY PAGE WILL BE THERE
    last_page = count_of_events // 10
    pages = []
    if count_of_events % 10 > 0:
        last_page += 1
    for index in range(1, last_page+1):
            pages.append(index)

    # GET USER'S TASKS
    if count_of_events == 0:
        log_of_user = False
        last_page = 1
        pages = [1]
        events_of_page = []
    else:
        if request.GET.get('page'):
            page_number = int(request.GET.get('page'))
            first_index_of_the_page = (page_number-1)*10
            final_index_of_the_page = 10*page_number-1
            if final_index_of_the_page >= count_of_events:
                final_index_of_the_page = count_of_events-1
            events_of_page = []

            for i in range(first_index_of_the_page, final_index_of_the_page+1):
                events_of_page.append(log_of_user[i])
        else:
            page_number = 1
            first_index_of_the_page = 0
            final_index_of_the_page = 9
            if final_index_of_the_page >= count_of_events:
                final_index_of_the_page = count_of_events-1
            events_of_page = []

            for i in range(first_index_of_the_page, final_index_of_the_page+1):
                events_of_page.append(log_of_user[i])

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'current_language': current_language,

        'log': events_of_page,
        'pages': pages,
        'count': count_of_events,

        'is_nav': True,
    }

    return render(request, 'tasks/log.html', context)


# Crud operation, create new task
@login_required
def create_task(request):
    auth_stat = request.user.is_authenticated

    # AUTHENTICATED OR GUEST
    auth_stat = request.user.is_authenticated
    log_of_user = LogHistory.objects.filter(user=request.user).order_by('-datentime')
    if request.user.is_authenticated:
        if request.user.first_name or request.user.last_name:
            nickname = f'{request.user.first_name} {request.user.last_name}'
        else:
            nickname = 'Anonymous'
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

    # AUTHENTICATED OR GUEST
    auth_stat = request.user.is_authenticated
    log_of_user = LogHistory.objects.filter(user=request.user).order_by('-datentime')
    if request.user.is_authenticated:
        if request.user.first_name or request.user.last_name:
            nickname = f'{request.user.first_name} {request.user.last_name}'
        else:
            nickname = 'Anonymous'
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
    # GET URL PARAMETERS OR DEFAULT
    current_language = request.GET.get('lang') or 'english'

    # AUTHENTICATED OR GUEST
    auth_stat = request.user.is_authenticated
    log_of_user = LogHistory.objects.filter(user=request.user).order_by('-datentime')
    if request.user.is_authenticated:
        if request.user.first_name or request.user.last_name:
            nickname = f'{request.user.first_name} {request.user.last_name}'
        else:
            nickname = 'Anonymous'
    else:
        nickname = 'Guest'

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'current_language': current_language,

        'is_nav': True,
    }

    return render(request, 'tasks/about.html', context)


# opening the contact page
def contact(request):
    # GET URL PARAMETERS OR DEFAULT
    current_language = request.GET.get('lang') or 'english'

    # AUTHENTICATED OR GUEST
    auth_stat = request.user.is_authenticated
    log_of_user = LogHistory.objects.filter(user=request.user).order_by('-datentime')
    if request.user.is_authenticated:
        if request.user.first_name or request.user.last_name:
            nickname = f'{request.user.first_name} {request.user.last_name}'
        else:
            nickname = 'Anonymous'
    else:
        nickname = 'Guest'

    context = {
        'user': nickname,
        'auth_stat': auth_stat,

        'current_language': current_language,

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
