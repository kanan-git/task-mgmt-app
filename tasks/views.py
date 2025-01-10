from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm


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
