from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    events = Events.objects.all()
    return render(request, 'website/index.html', {'events': events})