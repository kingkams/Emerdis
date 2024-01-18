from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, TemplateView,View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import People, Assembly
from .forms import RegistrationPeopleForm
from . import verify


class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationPeopleForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        context['contacts'] = self.request.GET.get('contact')
        return context

    #   def form_valid(self, form):
    #      user = form.save()
    #     verify.send(form.cleaned_data.get('contact'))
    # prints the email entered in the form
    #    return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProductLogin(LoginView):
    template_name = "registration/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_people:
            return reverse_lazy('post:Posts')
        elif self.request.user.is_assembly:
            return reverse_lazy('post:AssemPost')


class ProfileView(UpdateView, LoginRequiredMixin):
    model = People
    fields = ['contact', 'lastname', 'town', 'username']
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user


class HomeView(TemplateView):
    template_name = '../templates/home.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_people:
            return reverse_lazy('post:Posts')
        elif self.request.user.is_assembly:
            return reverse_lazy('post:AssemPost')
