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
       
        return dict(id=i, file=f, caption=caption)
    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        return dict(photo=p)
