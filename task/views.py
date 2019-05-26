from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy, reverse


def index(request):
    template = loader.get_template('task/task_list.html')
    allTasks = Task.objects.all()
    context = {
        'allTasks': allTasks
    }
    return HttpResponse(template.render(context, request))


class TaskCreate(CreateView):
    model = Task
    fields = ['Title', 'Description']


class TaskDetails(DetailView):
    model = Task
    template_name = 'task/details.html'


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task:index')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse('task:index'))
        else:
            return super(TaskDelete, self).post(request, *args, **kwargs)


def update_status(request):
    id = request.POST.get("card_id", default=None)
    status = request.POST.get("status", default=None)
    card = Task.objects.get(pk=id)
    card.Status = status
    card.save()
    template = loader.get_template('task/task_list.html')
    allTasks = Task.objects.all()
    context = {
        'allTasks': allTasks
    }
    return HttpResponse(template.render(context, request))
