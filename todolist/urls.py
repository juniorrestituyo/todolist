from django.urls import path
from . import views

urlpatterns = [
    path("", views.todolistPage, name="todo-list"),
    path("create/", views.createTask, name="create"),
    path("delete-task/<str:pk>/", views.deleteTask, name="delete-task"),
    path("check/<str:pk>/", views.check, name="check"),
    path("uncheck/<str:pk>/", views.uncheck, name="uncheck"),
]