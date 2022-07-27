from django import forms
from django.forms import TextInput, DateTimeInput, Textarea, NumberInput

from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date',
                  'is_organiser', 'website_url', 'address', 'long', 'lat', 'contact_num']
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
