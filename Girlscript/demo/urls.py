from django.conf.urls import url
from . import views

app_name = 'demo'
urlpatterns = [
    url(r'^home/$',views.home,name="home"),
    url(r'^about/$',views.about,name="about"),
    #url(r'^events/$',views.events,name="events"),
    url(r'^contact/$',views.contact,name="contact"),
    url(r'^donate/$',views.donate,name="donate"),
]
