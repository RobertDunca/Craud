from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.list import MultipleObjectMixin
from django.core.paginator import Paginator

from trip.filters import EventFilter, RestaurantFilter
from trip.forms import EventForm, ReviewForm, ThingToDoForm
from trip.models import Event, Restaurant, Review, ThingToDo


# class FilteredListView(ListView):
#     filter_class = None
#     filtered_set = None
#     fs_set = None
#     min_rating = 1
#
#     def __init__(self):
#         super().__init__()
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filtered_set = self.filter_class(self.request.GET, queryset=queryset)
#         return self.filtered_set.qs
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         objects = self.get_queryset()
#
#         self.min_rating = int(self.request.GET.get('min_rating', 1))
#
#         self.fs_set = filter_sort_objects(list(objects), self.min_rating)
#         paginator = self.get_paginator(self.fs_set, self.paginate_by)
#         self.fs_set = paginator.page(self.request.GET.get('page', 1)).object_list
#
#         # paginated_filtered_objects = Paginator(self.fs_set.qs, 5)
#
#         data['filter'] = self.filtered_set
#         data['min_rating'] = self.min_rating
#         data[self.context_object_name] = self.fs_set
#
#         return data


class ReviewCreateView(LoginRequiredMixin, CreateView):
    template_name = 'reviews/create_review.html'
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        if form.is_valid():
            review = form.save(commit=False)
            review.user = self.request.user
            review.save()
            review_model = self.request.POST.get('review_model')
            id_ = self.request.POST.get('id')
            if review_model == 'event':
                event = Event.objects.get(pk=id_)
                event.reviews.add(review)
                event.save()
            elif review_model == 'restaurant':
                restaurant = Restaurant.objects.get(pk=id_)
                restaurant.reviews.add(review)
                restaurant.save()
            elif review_model == 'thing':
                thing_to_do = ThingToDo.objects.get(pk=id_)
                thing_to_do.reviews.add(review)
                thing_to_do.save()
            return redirect(self.get_success_url())


class EventCreateView(LoginRequiredMixin, CreateView):
    template_name = 'events/create_event.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('create_new_event')


class EventListView(ListView):
    template_name = 'events/list_of_events.html'
    model = Event
    context_object_name = 'all_events'
    paginate_by = 5
    filter_class = EventFilter


class EventDetailView(DetailView):
    template_name = 'events/event_details.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = ReviewForm()
        return context


class RestaurantCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'restaurants/create_restaurant.html'
    model = Restaurant
    form_class = EventForm
    success_url = reverse_lazy('create_new_restaurant')


class RestaurantListView(ListView):
    template_name = 'restaurants/list_of_restaurants.html'
    paginate_by = 5
    model = Restaurant
    context_object_name = 'all_restaurants'
    filter_class = RestaurantFilter

    # def get_queryset(self):
    #     # restaurants = Restaurant.objects.all()
    #     queryset = super().get_queryset()
    #     restaurant_filter = RestaurantFilter(self.request.GET, queryset=queryset)
    #     # self.get_paginator()
    #     # restaurants = Restaurant.objects.all()
    #     return restaurant_filter.qs

    def get_context_data(self, **kwargs):
        data = super(RestaurantListView, self).get_context_data()
        # restaurants = self.get_queryset()

        filtered_restaurants = RestaurantFilter(self.request.GET, queryset=self.get_queryset())
        paginated_filtered_restaurants = Paginator(filtered_restaurants.qs, self.paginate_by)
        page_number = self.request.GET.get('page')
        restaurant_page_obj = paginated_filtered_restaurants.get_page(page_number)
        # restaurants = list(restaurants)
        #
        # min_rating = int(self.request.GET.get('min_rating', 1))
        #
        # restaurants = filter_sort_objects(restaurants, min_rating)
        # paginator = self.get_paginator(restaurants, self.paginate_by)
        # restaurants = paginator.page(self.request.GET.get('page', 1)).object_list


        # data['min_rating'] = min_rating
        data['filtered_restaurants'] = filtered_restaurants
        # data['restaurant_filter'] = restaurant_filter
        data['restaurant_page_obj'] = restaurant_page_obj

        return data


class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurant_details.html'
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = ReviewForm()
        return context


class ThingToDoCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'things_to_do/create_ttd.html'
    model = ThingToDo
    form_class = ThingToDoForm
    success_url = reverse_lazy('create_new_ttd')


class ThingToDoListView(ListView):
    template_name = 'things_to_do/list_of_ttd.html'
    model = ThingToDo
    context_object_name = 'all_ttd'


def filter_sort_objects(objects, min_rating=1):
    objects = list(filter(lambda obj: obj.average_rating() >= min_rating, objects))
    objects.sort(key=lambda obj: obj.average_rating(), reverse=True)
    return objects


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        all_restaurants = Restaurant.objects.all()
        count_restaurants = all_restaurants.count()

        all_events = Event.objects.all()
        count_events = all_events.count()

        data = {'restaurants': filter_sort_objects(objects=all_restaurants)[:min(count_restaurants, 3)],
                'events': filter_sort_objects(objects=all_events)[:min(count_events, 3)],
                }
        return data
