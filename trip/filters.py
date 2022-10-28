from trip.models import Event, Restaurant, ThingToDo
import django_filters


class TripFilter(django_filters.FilterSet):
    CHOICES = (
        ('created', 'All'),
        ('rating', 'Rating'),
        ('alphabetical', 'A-Z'),
    )

    avg_rating = django_filters.NumberFilter(lookup_expr='gt', label='Minimum rating', max_value=5, min_value=0)
    ordering = django_filters.ChoiceFilter(label='Order by', method='order', choices=CHOICES)

    class Meta:
        fields = ['avg_rating', 'ordering']

    def __init__(self, *args, **kwargs):
        super(TripFilter, self).__init__(*args, **kwargs)
        self.filters['avg_rating'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['ordering'].field.widget.attrs.update({'class': 'form-control', 'onchange': 'submit()'})

    def order(self, qs, name, value):
        if value == 'created':
            expression = 'created_at'
        elif value == 'rating':
            expression = '-avg_rating'
        else:
            expression = 'name'

        return qs.order_by(expression)


class RestaurantFilter(TripFilter):
    CATEGORIES = Restaurant.restaurant_options

    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    type = django_filters.ChoiceFilter(label='Category', choices=CATEGORIES)

    class Meta:
        model = Restaurant
        fields = ['name', 'type', 'avg_rating', 'ordering']

    def __init__(self, *args, **kwargs):
        super(RestaurantFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search restaurant'})
        self.filters['type'].field.widget.attrs.update({'class': 'form-select'})


class EventFilter(TripFilter):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')

    class Meta:
        model = Event
        fields = ['name',  'avg_rating', 'ordering']

    def __init__(self, *args, **kwargs):
        super(EventFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search event'})


class ThingToDoFilter(TripFilter):
    CATEGORIES = ThingToDo.category_options

    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    type = django_filters.ChoiceFilter(label='Category', choices=CATEGORIES)

    class Meta:
        model = Restaurant
        fields = ['name', 'type', 'avg_rating', 'ordering']

    def __init__(self, *args, **kwargs):
        super(ThingToDoFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Search restaurant'})
        self.filters['type'].field.widget.attrs.update({'class': 'form-select'})
