from json import loads, dump
from django.core.management.base import BaseCommand
from hero.models import Superhero, Article
from csv import writer

class Command(BaseCommand):

    def handle(self, *args, **options):
        save_data()


def save_data():
    data = [b for b in Superhero.objects.all().values()]

    with open('hero_objects.json', "w") as f:
        dump(data, f, indent=4)
    
    with open('hero_objects.csv', newline='') as f:
        writer(f).writerows(data)
        
    data = [b for b in Article.objects.all().values()]

    with open('article_objects.json', "w") as f:
        dump(data, f, indent=4)
        
    with open('article_objects.csv', newline='') as f:
        writer(f).writerows(data)