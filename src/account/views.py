from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import UserRegistrationForm


class UserLogin(LoginView):
    ...


class UserLogout(LogoutView):
    ...


class UserRegistration(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("quiz:index")

    def form_valid(self, form):
        _form = super().form_valid(form)
        login(self.request, self.object)
        return _form
