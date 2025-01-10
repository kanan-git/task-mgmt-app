from django.urls import path

from tasks import views as tasks_view

urlpatterns =[
    # path group for main pages
    path('', tasks_view.tasks_list, name='tasks_list'),
    path('dashboard/', tasks_view.dashboard, name='dashboard'),
    path('log', tasks_view.log, name='log'),

    # path group for crud operations
    path('create_task/', tasks_view.create_task, name='create_task'),
    path('read_task/<int:pk>', tasks_view.read_task, name='read_task'),
    path('update_task/<int:pk>', tasks_view.update_task, name='update_task'),
    path('delete_task/<int:pk>', tasks_view.delete_task, name='delete_task'),

    # path group for rest of pages
    path('about/', tasks_view.about, name='about'),
    path('contact/', tasks_view.contact, name='contact')
]
