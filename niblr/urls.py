from django.conf.urls import url

from . import views

urlpatterns = [
    url('^detail$', views.RestaurantDetailView.as_view()),
    url('^list$', views.RestaurantListView.as_view(), name="restaurant_list"),
]