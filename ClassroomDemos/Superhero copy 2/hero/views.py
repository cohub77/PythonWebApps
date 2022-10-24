from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

from .models import Superhero, User


class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero
    context_object_name = "heroes"


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero
    context_object_name = "hero"


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = ['name', 'identity', 'description',
              'image', 'strengths', 'weaknesses']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = '..'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class MyHeroesView(LoginRequiredMixin, ListView):
    model = Superhero
    template_name = "registration/my_heroes.html"
    context_object_name = "heroes"
    fields = '__all__'


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_detail.html"


# class ArticleCreateView(LoginRequiredMixin, CreateView):
#   template_name = "article_add.html"
#    model = Article
#    fields = '__all__'
#
#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile.html"
    model = User
    fields = '__all__'
