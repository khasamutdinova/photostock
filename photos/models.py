from django.db import models
from django.conf import settings
from django.utils import timezone

class Photo(models.Model):
    title=models.CharField = models.CharField(max_length=100)
    image=models.ImageField = models.ImageField(upload_to=None)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField = models.CharField(max_length=200)

def publish(self):
        self.published_date = timezone.now()
        self.save()

def __str__(self):
        return self.title


