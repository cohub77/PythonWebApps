from django.urls import path
from hero.views import HulkView, IndexView, IronManView, BlackWidow, HindsightLad, ThreeDMan

urlpatterns = [
    path('hulk',        HulkView.as_view()),
    path('ironman',        IronManView.as_view()),
    path('blackwidow',        BlackWidow.as_view()),
    path('hindsightlad',        HindsightLad.as_view()),
    path('3dman',        ThreeDMan.as_view()),
    path('',            IndexView.as_view()),
]