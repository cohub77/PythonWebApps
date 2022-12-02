from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import CarouselView, DeleteView, DetailView, ListView, CreateView, UpdateView


urlpatterns = [

    # Photo
    path('photo/',                      ListView.as_view(),    name='photo_list'),
    path('photo/<int:pk>',              DetailView.as_view(),  name='photo_detail'),
    path('photo/add',                   CreateView.as_view(),  name='photo_add'),
    path('photo/<int:pk>/',             UpdateView.as_view(),  name='photo_edit'),
    path('photo/<int:pk>/delete',       DeleteView.as_view(),  name='photo_delete'),

    # Photo Display
    path('photo/carousel',              CarouselView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
