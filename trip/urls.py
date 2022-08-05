from django.urls import path

from trip import views

urlpatterns = [
    path('create-event/', views.EventCreateView.as_view(), name='create_new_event'),
    path('events/', views.EventListView.as_view(), name='all_events'),
    path('restaurants/', views.RestaurantListView.as_view(), name='all_restaurants'),
]

