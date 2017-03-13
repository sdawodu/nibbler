from django.contrib import admin

from .models import Cuisine, Restaurant, UserRating


admin.site.register(Cuisine)
admin.site.register(Restaurant)
admin.site.register(UserRating)
