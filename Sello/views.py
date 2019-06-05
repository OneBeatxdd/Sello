from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


# Create your views here.
def index(request):

    return redirect('task:index')


def stickers(request):
    template = loader.get_template('sticker/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))
