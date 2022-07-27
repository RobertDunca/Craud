from django import forms
from django.forms import TextInput, Textarea, NumberInput, Select

from things_to_do.models import ThingsToDo


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = ThingsToDo
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
