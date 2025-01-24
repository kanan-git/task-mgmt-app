from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}')
            return redirect('tasks_list')
        else:
            messages.info(request, f'Your username or password is incorrect')

    form = AuthenticationForm()

    context = {
        'user': 'guest',

        'untitled_data': 'empty',

        'is_nav': False,

        'form': form,
    }

    return render(request, 'accounts/sign_in.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            messages.error(request, form.errors)
            return redirect('sign_up')
    else:
        form = UserCreationForm()

        context = {
            'user': 'guest',

            'untitled_data': 'empty',

            'is_nav': False,

            'creation_form': form
        }

        return render(request, 'accounts/sign_up.html', context)


def sign_out(request):
    logout(request)
    return redirect('tasks_list')
