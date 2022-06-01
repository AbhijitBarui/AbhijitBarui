from re import M
from django.db import models

Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
)

class Testimonial(models.Model):
    rating = models.IntegerField(choices=Rating_CHOICES, default=3)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message[:20]


# star_rating                 integerfield        integerchoices
# name                        charfield           100
# position                    charfield           50
# message                     textfield           
# updated                     datetimefield       auto_now true
# created                     datetimefield       auto_now_add true