from django.views.generic import RedirectView
from django.urls import path

from hero.views import PhotoDetailView, PhotoListView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='photo/')),

    # Photos
    path('photo/', PhotoListView.as_view()),
    path('photo/<int:id>', PhotoDetailView.as_view()),
]
