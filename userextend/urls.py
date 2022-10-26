from django.urls import path

from userextend import views

urlpatterns = [
    path('create-user/', views.UserExtendCreateView.as_view(), name='create_user'),
    path('user-details/<int:pk>/', views.UserExtendDetailView.as_view(), name='user_details'),
    path('update-user/<int:pk>/', views.UserExtendUpdateView.as_view(), name='update_user'),
    path('delete-user/<int:pk>/', views.UserExtendDeleteView.as_view(), name='delete_user'),
    path('user-events/<int:pk>/', views.get_events_per_user, name='user_events')
]
