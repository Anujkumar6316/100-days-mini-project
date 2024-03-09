from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # user will have one to many realtionship with task
    # .cascaede will delete the task of that user if the user is deleted we can keep the task by using set_null
    user =  models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=User.username)

    title = models.CharField(max_length=200, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['status']