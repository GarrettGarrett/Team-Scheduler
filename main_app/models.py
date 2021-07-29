from django.db import models


class Schedule(models.Model):
    name = models.CharField(max_length=100)

    SundayStart = models.IntegerField(default='0', verbose_name='Sunday Start Time')
    SundayEnd = models.IntegerField(default='0', verbose_name='Sunday End Time')
    
    MondayStart = models.IntegerField(default='0', verbose_name='Monday Start Time')
    MondayEnd = models.IntegerField(default='0', verbose_name='Monday End Time')

    TuesdayStart = models.IntegerField(default='0', verbose_name='Tuesday Start Time')
    TuesdayEnd = models.IntegerField(default='0', verbose_name='Tuesday End Time')

    WednesdayStart = models.IntegerField(default='0', verbose_name='Wednesday Start Time')
    WednesdayEnd = models.IntegerField(default='0', verbose_name='Wednesday End Time')

    ThursdayStart = models.IntegerField(default='0', verbose_name='Thursday Start Time')
    ThursdayEnd = models.IntegerField(default='0', verbose_name='Thursday End Time')

    FridayStart = models.IntegerField(default='0', verbose_name='Friday Start Time')
    FridayEnd = models.IntegerField(default='0', verbose_name='Friday End Time')

    SaturdayStart = models.IntegerField(default='0', verbose_name='Saturday Start Time')
    SaturdayEnd = models.IntegerField(default='0', verbose_name='Saturday End Time')

    TotalTime = models.IntegerField(default='0', verbose_name='Total Time')

    def __str__(self):
        return self.name

 