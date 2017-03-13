from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField


CHEAP = '0'
MIDRANGE = '1'
EXPENSIVE = '2'
PRICE_CLASSIFICATION = (
    (CHEAP, 'Cheap'),
    (MIDRANGE, 'Mid-range'),
    (EXPENSIVE, 'Expensive'),
)


class Cuisine(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    position = GeopositionField()
    cuisine_category = models.ManyToManyField(Cuisine)
    price_classification = models.CharField(
        choices=PRICE_CLASSIFICATION,
        default=MIDRANGE,
        max_length=12,
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'position')


class UserRating(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    star_rating = models.IntegerField(default=5)
    comments = models.TextField(
        max_length=140,
        help_text="Keep it under 140 chars"
    )
    author = models.ForeignKey(User)

    def __str__(self):
        return "{0}-{1}".format(self.author, self.restaurant)

    class Meta:
        unique_together = ('author', 'restaurant')
