from django.db import models

# Create your models here.
class Places(models.Model):
    Name = models.CharField(max_length=20)
    Summery = models.TextField()

    class Meta:
        verbose_name_plural= "Places"
    def __str__(self):
        return self.Name