from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.index),
    path('routines/', v.routine_view, name='routine-list'),
    path('routines/<int:pk>/', v.routine_detail, name='routine-detail'),
    path('todos/', v.todo_view, name='todo-list'),
    path('todos/<int:pk>/', v.todo_detail, name='todo-detail'),

    path('all-routines/', v.all_routines, name='all-routines'),
    path('all-todos/', v.all_todos, name='all-todos'),
]
