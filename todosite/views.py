from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import Http404
from django.views.generic import TemplateView
# Create your views here.


def submit(request):
    try:
        task_list = Task.objects.all()
        if request.method == "POST":
            formtask = TaskForm(request.POST)
            if formtask.is_valid():
                formtask.save()
                return redirect('todosite')
        formtask = TaskForm()
        page = {
            "formtask": formtask,
            "task_list": task_list,
            "title": "TASK LIST",
        }
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'pages/todowebsite.html', page)

def removetask(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    return redirect('todosite')

def updatetask(request, item_id):
    # item = Task.objects.get(id=item_id)
    # item.title = "Updated"
    # item.save()
    # return redirect('todosite')
    subitem = "???"
    item = Task.objects.get(id=item_id)
    item.title = subitem
    item.save()
    return redirect('todosite')
