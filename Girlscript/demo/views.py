from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
#from .models import Bill,UserProfile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

app='demo'

def home(request):
    return render(request, 'index.html', {})

def about(request):
    p = "<h1>About Us</h1>"
    return HttpResponse(p)

def contact(request):
    p = "<h1>Contact Us</h1>"
    return HttpResponse(p)


def donate(request):
    p = "<h1>Donate</h1>"
    return HttpResponse(p)
