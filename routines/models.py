from django.db import models
from datetime import datetime

class Routine(models.Model):
    day = models.CharField(max_length=10, default=datetime.today().strftime('%A'))
    sixam = models.CharField(max_length=200, default= 'Workout')
    sevenam = models.CharField(max_length=200, default='Breakfast')
    eightam = models.CharField(max_length=200, default='interview questions')
    nineam = models.CharField(max_length=200, default='interview questions')
    tenam = models.CharField(max_length=200, default='Aptitude')
    elevenam = models.CharField(max_length=200, default='data structures')
    twelveam = models.CharField(max_length=200, default='algorithms')
    onepm = models.CharField(max_length=200, default='Lunch')
    twopm = models.CharField(max_length=200, default='internship')
    threepm = models.CharField(max_length=200, default='internship')
    fourpm = models.CharField(max_length=200, default='internship')
    fivepm = models.CharField(max_length=200, default='Break')
    sixpm = models.CharField(max_length=200, default='self skill ++')
    sevenpm = models.CharField(max_length=200, default='self skill ++')
    eightpm = models.CharField(max_length=200, default='self skill ++')
    ninepm = models.CharField(max_length=200, default='Dinner')
    tenpm = models.CharField(max_length=200, default='Application process')
    elevenpm = models.CharField(max_length=200, default='Day Review')
    twelvepm = models.CharField(max_length=200, default='Sleep')

    def __str__(self) -> str:
        return self.day