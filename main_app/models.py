from django.db import models

# Create your models here.
class Schedule(models.Model):
    name = models.CharField(max_length=100)
    SundayStart = models.IntegerField()
    SundayEnd = models.IntegerField()

    def __str__(self):
        return self.name
