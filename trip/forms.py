from django import forms
from django.forms import TextInput, DateTimeInput, Textarea, NumberInput, Select

from trip.models import Event, Restaurant, ThingToDo, Review


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date',
                  'user_is_organiser', 'website_url', 'address', 'long', 'lat', 'contact_num']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter event name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter event description', 'class': 'form-control'}),
            'start_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'website_url': TextInput(attrs={'placeholder': 'Please enter event website url', 'class': 'form-control',
                                            'required': False}),
            'contact_num': TextInput(attrs={'placeholder': 'Please enter event contact number',
                                            'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Please enter event address', 'class': 'form-control'}),
            'long': NumberInput(attrs={'placeholder': 'Please enter event longitude', 'class': 'form-control',
                                       'required': False}),
            'lat': NumberInput(attrs={'placeholder': 'Please enter event latitude', 'class': 'form-control',
                                      'required': False})

        }


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'type', 'description', 'website_url', 'address', 'long', 'lat', 'contact_num']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter restaurant name', 'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'placeholder': 'Please enter restaurant description',
                                           'class': 'form-control'}),
            'website_url': TextInput(attrs={'placeholder': 'Please enter restaurant website url',
                                            'class': 'form-control', 'required': False}),
            'contact_num': TextInput(attrs={'placeholder': 'Please enter restaurant contact number',
                                            'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Please enter restaurant address', 'class': 'form-control'}),
            'long': NumberInput(attrs={'placeholder': 'Please enter restaurant longitude', 'class': 'form-control',
                                       'required': False}),
            'lat': NumberInput(attrs={'placeholder': 'Please enter restaurant latitude', 'class': 'form-control',
                                      'required': False})
            }


class ThingToDoForm(forms.ModelForm):
    class Meta:
        model = ThingToDo
        fields = ['name', 'type', 'description', 'website_url', 'address', 'long', 'lat', 'contact_num']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter activity name', 'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'placeholder': 'Please enter activity description',
                                           'class': 'form-control'}),
            'website_url': TextInput(attrs={'placeholder': 'Please enter website url',
                                            'class': 'form-control', 'required': False}),
            'contact_num': TextInput(attrs={'placeholder': 'Please enter contact number',
                                            'class': 'form-control', 'required': False}),
            'address': TextInput(attrs={'placeholder': 'Please enter address', 'class': 'form-control'}),
            'long': NumberInput(attrs={'placeholder': 'Please enter longitude', 'class': 'form-control',
                                       'required': False}),
            'lat': NumberInput(attrs={'placeholder': 'Please enter latitude', 'class': 'form-control',
                                      'required': False})
            }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
            'comment': Textarea(attrs={'placeholder': 'Please enter a comment',
                                       'class': 'form-control', 'required': False}),
        }
