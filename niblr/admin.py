from django.contrib import admin

from .models import Cuisine, Restaurant, UserRating


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price_classification'
    )
    filter_horizontal = (
        'cuisine_category',
    )


@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'restaurant',
        'star_rating',
    )
