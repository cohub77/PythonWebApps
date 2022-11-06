from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, SignUpView, MyHeroesView, RedirectView, HomeView, ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView 
from django.contrib import admin

urlpatterns = [
    path('', HomeView.as_view(),    name='home_list'),
    
    path('hero/',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),

    path('article/',                ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',        ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',             ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/edit',       ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(),  name='article_delete'),

    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/your-heroes", MyHeroesView.as_view(), name="my_heroes"),
    path('accounts/profile/', RedirectView.as_view(url='../..')),

    # Admin views for users
    path('admin/', admin.site.urls),
    # path('admin/', include('admin.site.urls')),   Don't do this!

]
