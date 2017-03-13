from django.contrib import admin

from .models import Cuisine, Restaurant, UserRating


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price_classification'
    )


@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    pass
