<<<<<<< HEAD
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content= models.TextField(max_length=1000, blank=False, null=False)
    time_create = models.DateTimeField(default=timezone.now())
    def str(self):
        return self.title
    def str(self):
        return self.content
=======
>>>>>>> a01386fb3daae376bc29308e2e113b1514907a73
