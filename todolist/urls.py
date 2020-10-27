from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('add',views.addTodoItem,name='add'),
   path('completed/<todo_id>',views.completedTodo,name='completed'),
   path('deletecompleted',views.deleteCompleted,name='deletecompleted'),
   path('deleteall',views.deleteAll,name='deleteall'),
   path('update_task/<str:pk>/',views.updateTask, name='update_task'),
   path('delete_task/<str:pk>/',views.deleteTask, name='delete_task')
]


