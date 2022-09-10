from django.urls import path
from hero.views import HulkView, IndexView, IronManView, BlackWidow

urlpatterns = [
    path('hulk',        HulkView.as_view()),
    path('ironman',        IronManView.as_view()),
    path('blackwidow',        BlackWidow.as_view()),
    path('',            IndexView.as_view()),
]