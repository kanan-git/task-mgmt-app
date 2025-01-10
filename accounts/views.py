from django.shortcuts import render


def sign_in(request):
    context = {
        'untitled_data': 'empty'
    }
    return render(request, 'accounts/sign_in.html', context)
