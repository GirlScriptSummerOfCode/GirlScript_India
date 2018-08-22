from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/<int:event_id>', views.general_events, name='events'),
]
