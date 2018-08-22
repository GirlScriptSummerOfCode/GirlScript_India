from django.db import models

# Create your models here.

#This section is for Positions on the map
class Positions(models.Model):
    city_name = models.CharField(null=False,max_length=100)
    latitude = models.FloatField(null=False,default=None)
    longitude = models.FloatField(null=False,default=None)
    url = models.URLField()

#This section is for the events
class Events(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(null=False,max_length=250)
    description = models.TextField(null=False)
    summary = models.TextField(null=False)
    featured_image = models.TextField(null=False)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

#This section confines to different pictures in different events
class Pictures(models.Model):
    picture_id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    # src=models.ImageField() #requires pillow library
    src = models.TextField(null=False)
    alt = models.CharField(null=False,max_length=100)

#This section is for different Faq in different events
class FAQ(models.Model):
    faq_id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    question = models.CharField(null=False,max_length=200)
    answer = models.TextField()

#This section is for the schedule for each event
class Schedule(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    content = models.TextField()

#This section is the testimonial section
class Testimonial(models.Model):
    uid = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50)
    headline = models.CharField(max_length=200)
    content = models.TextField() 

#Sponsor class is for General and not Event Specific
class Sponsors(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.URLField()
    img = models.TextField()


