from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.core.paginator import Paginator

from trip.filters import EventFilter, RestaurantFilter
from trip.forms import EventForm, ReviewForm, ThingToDoForm
from trip.models import Event, Restaurant, Review, ThingToDo


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
                event.full_clean()
                event.save()
            elif review_model == 'restaurant':
                restaurant = Restaurant.objects.get(pk=id_)
                restaurant.reviews.add(review)
                restaurant.full_clean()
                restaurant.save()
            elif review_model == 'thing':
                thing_to_do = ThingToDo.objects.get(pk=id_)
                thing_to_do.reviews.add(review)
                thing_to_do.full_clean()
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

    def get_context_data(self, **kwargs):
        data = super(EventListView, self).get_context_data()

        filtered_events = EventFilter(self.request.GET, queryset=Event.objects.all())

        paginated_filtered_events = Paginator(filtered_events.qs, self.paginate_by)
        page_number = self.request.GET.get('page')
        event_page_obj = paginated_filtered_events.get_page(page_number)

        data['filtered_events'] = filtered_events
        data['event_page_obj'] = event_page_obj

        return data


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

    def get_context_data(self, **kwargs):
        data = super(RestaurantListView, self).get_context_data()

        filtered_restaurants = RestaurantFilter(self.request.GET, queryset=Restaurant.objects.all())

        paginated_filtered_restaurants = Paginator(filtered_restaurants.qs, self.paginate_by)
        page_number = self.request.GET.get('page')
        restaurant_page_obj = paginated_filtered_restaurants.get_page(page_number)

        data['filtered_restaurants'] = filtered_restaurants
        data['restaurant_page_obj'] = restaurant_page_obj

        return data


class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurant_details.html'
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        all_restaurants = Restaurant.objects.all()
        type_restaurants = filter(lambda r: r.type == self.object.type and r != self.object, all_restaurants)
        type_restaurants = sorted(type_restaurants, key=lambda obj: obj.avg_rating)
        restaurants = []
        for n, restaurant in enumerate(type_restaurants):
            if n <= 4:
                restaurants.append(restaurant)

        context['type_restaurants'] = restaurants
        context['form'] = ReviewForm()

        return context


class ThingToDoCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'things_to_do/create_ttd.html'
    model = ThingToDo
    form_class = ThingToDoForm
    success_url = reverse_lazy('create_new_ttd')


class ThingToDoListView(ListView):
    template_name = 'things_to_do/all_ttd.html'
    model = ThingToDo
    context_object_name = 'all_ttd'


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'
