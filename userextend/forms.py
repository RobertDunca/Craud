from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput

from userextend.models import User


class UserExtendForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email',
        ]

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'username': TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': None,
            'email': None,
            'first_name': None,
            'last_name': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
