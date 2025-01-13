from django.shortcuts import render


def sign_in(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'accounts/sign_in.html', context)


def sign_up(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'accounts/sign_up.html', context)
