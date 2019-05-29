from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


# Create your views here.
def index(request):

    return redirect('task:index')


