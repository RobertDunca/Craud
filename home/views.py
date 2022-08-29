from django.shortcuts import render
from django.views.generic import TemplateView

from trip.models import Restaurant
from trip.views import filter_sort_restaurants


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        all_restaurants = Restaurant.objects.all()
        count = all_restaurants.count()
        return {'restaurants': filter_sort_restaurants(restaurants=all_restaurants)[:min(count, 3)]}
