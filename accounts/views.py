from django.shortcuts import render, redirect


def sign_in(request):
    context = {
        'user': 'guest',

        'untitled_data': 'empty',

        'is_nav': False,
    }
    return render(request, 'accounts/sign_in.html', context)


def sign_up(request):
    context = {
        'user': 'guest',

        'untitled_data': 'empty',

        'is_nav': False,
    }
    return render(request, 'accounts/sign_up.html', context)


def sign_out(request):
    return redirect('tasks/tasks_list')
