from django.db import models
from datetime import datetime

class Routine(models.Model):
    day = models.CharField(max_length=10, default=datetime.today().strftime('%A'))
    sixam = models.CharField(max_length=200, default= 'Workout')
    sevenam = models.CharField(max_length=200, default='Breakfast')
    eightam = models.CharField(max_length=200)
    nineam = models.CharField(max_length=200)
    tenam = models.CharField(max_length=200)
    elevenam = models.CharField(max_length=200)
    twelveam = models.CharField(max_length=200)
    onepm = models.CharField(max_length=200, default='Lunch')
    twopm = models.CharField(max_length=200)
    threepm = models.CharField(max_length=200)
    fourpm = models.CharField(max_length=200)
    fivepm = models.CharField(max_length=200, default='Break')
    sixpm = models.CharField(max_length=200)
    sevenpm = models.CharField(max_length=200)
    eightpm = models.CharField(max_length=200)
    ninepm = models.CharField(max_length=200, default='Dinner')
    tenpm = models.CharField(max_length=200, default='Application process')
    elevenpm = models.CharField(max_length=200, default='Day Review')
    twelvepm = models.CharField(max_length=200, default='Sleep')

    def __str__(self) -> str:
        return self.day