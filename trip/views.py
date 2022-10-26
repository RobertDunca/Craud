from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView, View
from django.core.paginator import Paginator
import folium

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

    def form_valid(self, form):
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = self.request.user
            event.save()

            return redirect(self.success_url)


class EventListView(ListView):
    template_name = 'events/list_of_events.html'
    model = Event
    context_object_name = 'all_events'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = super(EventListView, self).get_context_data()

        filtered_events = EventFilter(self.request.GET, queryset=Event.objects.all())
        event_page_obj = get_page_obj(self, filtered_events.qs)

        data['filtered_events'] = filtered_events
        data['event_page_obj'] = event_page_obj

        return data


class EventDetailView(DetailView):
    template_name = 'events/event_details.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        if self.object.lat and self.object.long:
            my_map = create_map(self)
            context['map'] = my_map

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
        restaurant_page_obj = get_page_obj(self, filtered_restaurants.qs)

        data['filtered_restaurants'] = filtered_restaurants
        data['restaurant_page_obj'] = restaurant_page_obj

        return data


class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurant_details.html'
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        other_restaurants = self.get_other_restaurants()

        if self.object.lat and self.object.long:
            my_map = create_map(self)
            context['map'] = my_map

        context['type_restaurants'] = other_restaurants
        context['form'] = ReviewForm()

        return context

    def get_other_restaurants(self):
        all_restaurants = Restaurant.objects.all().order_by('-avg_rating')
        type_restaurants = filter(lambda r: r.type == self.object.type and r != self.object, all_restaurants)
        restaurants = list(type_restaurants)[:4]

        return restaurants


class ThingToDoCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'things_to_do/create_ttd.html'
    model = ThingToDo
    form_class = ThingToDoForm
    success_url = reverse_lazy('create_new_ttd')


class ThingToDoListView(ListView):
    template_name = 'things_to_do/all_ttd.html'
    model = ThingToDo
    context_object_name = 'all_ttd'


class SearchListView(View):
    @classmethod
    def post(cls, request):
        searched = request.POST['searched']

        restaurants = Restaurant.objects.filter(name__contains=searched).order_by('-avg_rating')
        events = Event.objects.filter(name__contains=searched).order_by('-avg_rating')
        things_to_do = ThingToDo.objects.filter(name__contains=searched).order_by('-avg_rating')

        context = {
            'searched': searched,
            'restaurants': restaurants,
            'events': events,
            'things_to_do': things_to_do
        }

        return render(request, 'search.html', context)


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'


def get_page_obj(obj, filtered_qs):
    paginated_filtered_obj = Paginator(filtered_qs, obj.paginate_by)
    page_number = obj.request.GET.get('page')
    page_obj = paginated_filtered_obj.get_page(page_number)

    return page_obj


def create_map(obj):
    coordinates = [obj.object.lat, obj.object.long]
    my_map = folium.Map(coordinates, zoom_start=17)
    icon, color = 'circle', 'blue'

    if obj.model == Restaurant:
        icon, color = 'cutlery', 'red'
    elif obj.model == ThingToDo:
        icon, color = 'binoculars', 'green'
    elif obj.model == Event:
        icon, color = 'calendar', 'purple'

    folium.Marker(
        coordinates,
        tooltip=f'{obj.object.name}',
        icon=folium.Icon(color=color, prefix='fa', icon=icon)
    ).add_to(my_map)

    my_map = my_map._repr_html_()

    return my_map
