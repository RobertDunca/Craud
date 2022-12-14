from django.urls import path

from trip import views

urlpatterns = [
    path('create-event/', views.EventCreateView.as_view(), name='create_new_event'),
    path('events/', views.EventListView.as_view(), name='all_events'),
    path('event-details/<int:pk>/', views.EventDetailView.as_view(), name='event_details'),
    # path('user-events/', views.UserEventListView.as_view(), name='all_user_events'),
    path('restaurants/', views.RestaurantListView.as_view(), name='all_restaurants'),
    path('restaurant-details/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_details'),
    path('things-to-do/', views.ThingToDoListView.as_view(), name='all_ttd'),
    path('thing-to-do-details/<int:pk>/', views.ThingToDoDetailView.as_view(), name='ttd_details'),
    path('create-review/', views.ReviewCreateView.as_view(), name='create_review'),
    path('search/', views.SearchListView.as_view(), name='search'),
    path('', views.HomeTemplateView.as_view(), name='home'),

]
