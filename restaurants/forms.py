from django import forms
from django.forms import TextInput, Textarea, NumberInput, Select

from restaurants.models import Restaurant


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
