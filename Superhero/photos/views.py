from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, RedirectView, TemplateView, UpdateView

from .models import Photo


class PhotoView(RedirectView):
    url = reverse_lazy('photo_list')


class ListView(ListView):
    template_name = 'photo/list.html'
    model = Photo
    context_object_name = 'photos'


class CarouselView(TemplateView):
    template_name = 'photo/carousel.html'

    def get_context_data(self, **kwargs):
        photos = Photo.objects.all()
        carousel = carousel_data(photos)
        return dict(title='Carousel View', carousel=carousel)

class DetailView(DetailView):
    template_name = 'photo/detail.html'
    model = Photo
    context_object_name = 'photo'


class CreateView(LoginRequiredMixin, CreateView):
    template_name = "photo/add.html"
    model = Photo
    fields = '__all__'


class UpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photo/edit.html"
    model = Photo
    fields = '__all__'


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/delete.html'
    success_url = reverse_lazy('photo_list')

def carousel_data(photos):

    def photo_data(id, image):
        x = dict(image_url=f"/media/{image}", id=str(id), label=f"{image} {id}")
        if id == 0:
            x.update(active="active", aria='aria-current="true"')
        return x

    return [photo_data(id, photo.image) for id, photo in enumerate(photos)]



