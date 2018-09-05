from django.http import HttpResponse
from django.template import loader
from django.contrib import staticfiles
import os

def index(request):
    template = loader.get_template('index.html')
    #return HttpResponse(os.getcwd())
    context = {}
    return HttpResponse(template.render(context, request))

