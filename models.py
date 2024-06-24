from django.db import models
from django.utils import timezone

class EventManager(models.Manager):
    def upcoming_events(self):
        return self.filter(start_time__gte=timezone.now()).order_by('start_time')

    def past_events(self):
        return self.filter(start_time__lt=timezone.now()).order_by('-start_time')

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    objects = EventManager()

    def __str__(self):
        return self.title
