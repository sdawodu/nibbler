from django.shortcuts import render
from .models import Restaurant, Cuisine
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from jsonview.decorators import json_view

# Create your views here.
class RestaurantDetailView(DetailView):

    model = Restaurant

    @method_decorator(json_view)
    def dispatch(self, *args, **kwargs):
        return super(RestaurantDetailView, self).dispatch(*args, **kwargs)



class RestaurantListView(ListView):

    model = Restaurant

    @method_decorator(json_view)
    def dispatch(self, *args, **kwargs):
        return super(RestaurantListView, self).dispatch(*args, **kwargs)

    def get(self):

        qset = super(RestaurantListView, self).get_queryset()

        cuisine = self.request.GET.get('cuisine')
        cost = self.request.GET.get('cost')

        if cuisine:
            qset.filter(name__iexact=cuisine)


        if cost:
            int_cost = cost.count('£')
            limiter = cost[0]

            if limiter == '-':
                qset.filter(price_classification__lte=int_cost)

            if limiter == '+':
                qset.filter(price_classification__gte=int_cost)

        results = {
            'results': sorted(
                [i.dict_repr for i in qset],
                key=lambda x: x.avg_rating
            )
        }
        return results


