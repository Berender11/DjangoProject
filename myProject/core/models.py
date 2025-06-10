from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Survey(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    likes_django = models.BooleanField()
