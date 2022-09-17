from django.views.generic import TemplateView

class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }
        
class IronManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'id': 'Tony',
            'image': '/static/images/iron_man.jpg'
        }
class BlackWidow(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'id': 'idk',
            'image': '/static/images/black_widow.jpg'
        }
class HindsightLad(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hindsight Lad',
            'id': 'Carlton LaFroyge',
            'image': '/static/images/Origin-of-Hindsight-Lad.png'
        }
class ThreeDMan(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': '3-D Man',
            'id': 'Chuck Chandler',
            'image': '/static/images/3dman.png'
        }
        
class IndexView(TemplateView):
    template_name = 'heroes.html'        

