from django.urls import path

from accounts import views as accounts_view


urlpatterns = [
    path('sign_in/', accounts_view.sign_in, name='sign_in'),
    path('sign_up/', accounts_view.sign_up, name='sign_up'),
    path('sign_out/', accounts_view.sign_out, name='sign_out'),
]
