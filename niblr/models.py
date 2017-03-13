from django.db import models
from django.contrib.auth.models import User
from geoposition.fields import GeopositionField

from django.core.validators import MaxValueValidator, MinValueValidator


from . import utils


class Cuisine(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    position = GeopositionField()
    cuisine_category = models.ManyToManyField(Cuisine)
    price_classification = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)]
     )
    minutes_walk = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def avg_rating(self):
        all_ratings = [i.star_rating for i in self.userrating_set.all()]
        try:
            return (sum(all_ratings) / len(all_ratings))
        except ZeroDivisionError:
            return 0

    @property
    def dict_repr(self):
        return {
            'name': self.name,
            'cuisine_categories': [i.name for i in self.cuisine_category.all()],
            'price_classification': self.price_classification,
            'avg_rating': self.avg_rating,

            'comments': [i.comments for i in self.userrating_set.all()]
        }

    def save(self, *args, **kwargs):
        if not self.minutes_walk:
            self.minutes_walk = round(utils.get_walking_time(self.position) / 60)
        return super(Restaurant, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('name', 'position')
        ordering = ('-minutes_walk',)


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
