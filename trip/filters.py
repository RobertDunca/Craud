from trip.models import Event, Restaurant
import django_filters


class EventFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(EventFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search event'})


class RestaurantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    # min_rating = django_filters.NumberFilter(label='Minimum rating', method='filter_by_rating')

    class Meta:
        model = Restaurant
        fields = ['name', 'type']

    def __init__(self, *args, **kwargs):
        super(RestaurantFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search restaurant'})
        self.filters['type'].field.widget.attrs.update({'class': 'form-select'})


    # def filter_by_rating(self, queryset, name, value):
    #     queryset = list(filter(lambda obj: obj.average_rating() >= value, queryset))
    #     return queryset

