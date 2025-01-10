from django.urls import path

from accounts import views as accounts_view


urlpatterns = [
    path('sign_in/', accounts_view.sign_in, name='sign_in')
]
