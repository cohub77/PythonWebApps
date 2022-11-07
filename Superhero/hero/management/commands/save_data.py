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
        # CHANGE TO CSV
    data = [[hero.name, hero.identity, hero.description, hero.strengths,
            hero.weaknesses, hero.image,] for hero in Superhero.objects.all()]
        
    with open('hero_objects.csv', 'w', newline='') as f:
            writer(f).writerows(data)

        
    data = [b for b in Article.objects.all().values()]

    with open('article_objects.json', "w") as f:
        dump(data, f, indent=4)
        
    data = [[article.title, article.date, article.body, article.image,] 
            for article in Article.objects.all()]

    with open('article_objects.csv', 'w', newline='') as f:
            writer(f).writerows(data)