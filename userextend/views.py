from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from craud.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import User


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            create_user = form.save()
            message = f'Hello {create_user.first_name} {create_user.last_name}!' \
                      f' \n Welcome to Craud! \n Your username is: {create_user.username}'
            send_mail('Register confirmation', message, from_email=EMAIL_HOST_USER, recipient_list=[create_user.email])

        return redirect('home')
