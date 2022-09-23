from django.views.generic import TemplateView

from .models import Note
from pathlib import Path
from django.views.generic import TemplateView


def photo_list():
    def photo_details(i, f): 
        if i == 0 : caption = f'Caption for Photo 1 {i}' 
        elif i == 1: caption = f'Caption for Photo 2 {i}' 
        elif i == 2: caption = f'Caption for Photo 3 {i}' 
        elif i == 3: caption = f'Caption for Photo  4{i}' 
        elif i == 4: caption = f'Caption for Photo {i}' 
        else: None
        return dict(id=i, file=f)
    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos

class NoteListView(TemplateView):
    template_name = 'notes.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Note.objects.all()
        }


class NoteDetailView(TemplateView):
    template_name = 'note.html'

    def get_context_data(self, **kwargs):
        return {
            'note': Note.objects.get(pk=kwargs['pk'])
        }

class NoteDetailView(TemplateView):
    template_name = 'photo.html'
    def get_context_data(self, **kwargs):
        photos = photo_list()
        p = photos[kwargs['pk']]
        return dict(photo=p)
    