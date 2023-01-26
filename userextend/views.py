from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from craud.settings import EMAIL_HOST_USER
from trip.models import Event
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


class UserExtendDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = 'userextend/user_details.html'
    model = User

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id


class UserExtendUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'userextend/update_user.html'
    model = User
    form_class = UserExtendForm
    success_url = 'user_details'

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id


class UserExtendDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'userextend/delete_user.html'
    model = User
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id


@login_required
def get_events_per_user(request, pk):
    if request.user == User.objects.get(id=pk):
        events = Event.objects.filter(creator_id=pk)
        context = {'events': events}

        return render(request, 'events/user_events_list.html', context)
