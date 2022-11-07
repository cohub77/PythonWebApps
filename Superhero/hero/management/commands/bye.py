from django.core.management.base import BaseCommand
from json import loads
from pathlib import Path

from hero.models import Superhero, Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        bye()


def bye():
        Article.objects.all().delete()
