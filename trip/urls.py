from django.urls import path

from trip import views

urlpatterns = [
    path('create-event/', views.EventCreateView.as_view(), name='create_new_event'),
    path('events/', views.EventListView.as_view(), name='all_events'),
    path('event-details/<int:pk>/', views.EventDetailView.as_view(), name='event_details'),
    path('restaurants/', views.RestaurantListView.as_view(), name='all_restaurants'),
    path('create-review/', views.ReviewCreateView.as_view(), name='create_review'),
]

