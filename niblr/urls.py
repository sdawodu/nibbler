from django.conf.urls import url

from . import views

urlpatterns = [
    url('^detail$', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    url('^list$', views.RestaurantListView.as_view(), name="restaurant_list"),
    url('^random$', views.RestaurantRandomView.as_view(), name="restaurant_random"),
]
