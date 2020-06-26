from django.db import models

# Create your models here.
class Places(models.Model):
    Name = models.CharField(max_length=20)
    Summery = models.TextField()
