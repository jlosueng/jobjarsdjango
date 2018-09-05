from django.http import HttpResponse
from django.template import loader
import os

def index(request):
    template = loader.get_template('index.html')
    #return HttpResponse(os.getcwd())
    context = {}
    return HttpResponse(template.render(context, request))

def static(request, file):
    output=os.getcwd()
    #staticFile = open(request.path)
    #output = staticFile.read()
    return HttpResponse(output)