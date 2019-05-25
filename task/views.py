from django.http import HttpResponse
from django.template import loader
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


def index(request):
    template = loader.get_template('task/task_list.html')
    allTasks = Task.objects.all()
    context = {
        'allTasks': allTasks
    }
    return HttpResponse(template.render(context, request))
