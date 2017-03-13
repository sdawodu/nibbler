from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField


CHEAP = 0
MIDRANGE = 1
EXPENSIVE = 2
PRICE_CLASSIFICATION = (
    (CHEAP, 'Low'),
    (MIDRANGE, 'Normal'),
    (EXPENSIVE, 'High'),
)


class Cuisine(models.Model):
    name = models.CharField(max_length=64)

class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    position = GeopositionField()
    cuisine_category = models.ManyToManyField(Cuisine)
    price_classification = models.CharField(
        choices=PRICE_CLASSIFICATION,
        default=MIDRANGE,
        max_length=12,
    )


class UserRating(models.Model):
    star_rating = models.IntegerField(default=5)
    comments = models.TextField(max_length=140)
    author = models.ForeignKey(User)

