from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Feedback(models.Model):
    name = models.CharField(max_length=34)
    email = models.CharField(max_length=34)
    phno = models.IntegerField(null=True,blank=True)
    message = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} with email {self.email} left a feedback saying {self.message}"