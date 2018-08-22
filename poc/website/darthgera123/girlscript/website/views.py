from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    events = Events.objects.all()
    return render(request, 'website/index.html', {'events': events})

def general_events(request, event_id):
    event = Events.objects.get(pk=event_id)
    pics = Pictures.objects.filter(event_id=event_id)
    faq = FAQ.objects.filter(event_id=event_id)
    return render(request, 'website/events_page.html',{'event': event,'pics': pics, 'faqs': faq})