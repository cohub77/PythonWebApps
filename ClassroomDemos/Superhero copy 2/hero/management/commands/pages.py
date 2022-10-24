from requests import get
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = get('https://google.com')
        msg = f'Google: {len(response.text)}'
        print(msg)
