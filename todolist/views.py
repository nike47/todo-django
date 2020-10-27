from django.shortcuts import render,redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items':todo_items,'form':form}
    return render(request,'todolist/index.html',context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    #print(request.POST['text'])
    if form.is_valid():
        new_data = Todolist(text=request.POST['text'])
        new_data.save()
    return redirect('index')

def completedTodo(request,todo_id):
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')


def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')


def updateTask(request, pk):
    task = Todolist.objects.get(id=pk)
    form = TodoListForm(instance=task)

    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')


    context = {'form':form}

    return render(request, 'todolist/update_task.html',context)


def deleteTask(request, pk):
    task = Todolist.objects.get(id=pk)
    task.delete()
    return redirect('index')

    # if request.method == 'POST':
    #     task.delete()
    #     return redirect('index')
    # context = {'task':task}
    # return render(request, 'todolist/update_task.html',context)
