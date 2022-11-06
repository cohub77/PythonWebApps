from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.views.generic import RedirectView

class HomeView(ListView):
    template_name = "hero/home.html"
    model = Superhero
    
class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


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


class HeroDeleteView(DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')


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


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile.html"
    model = User
    fields = '__all__'

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = "articles"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "articles/add.html"
    model = Article
    fields = ['title', 'date', 'body', 'image']

    def form_valid(self, form):
        form.instance.investigator = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    success_url = '..'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "articles/edit.html"
    model = Article
    fields = '__all__'


class MyArticlesView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "registration/my_articles.html"
    context_object_name = "articles"
    fields = '__all__'