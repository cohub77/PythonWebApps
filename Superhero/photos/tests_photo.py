from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Author, Photo





class PhotoDataTest(TestCase):

    def setUp(self):
        self.user = test_user()
        self.photo1 = dict(title='title 1', image="photo1.png")
        self.photo2 = dict(title='title 2', image="photo2.png")

    def test_add_test(self):
        self.assertEqual(len(Photo.objects.all()), 0)
        Photo.objects.create(**self.photo1)
        x = Photo.objects.get(pk=1)
        self.assertEqual(x.title, self.photo1['title'])
        self.assertEqual(len(Photo.objects.all()), 1)

def user_args():
    return dict(username='TESTER', email='test@test.us', password='secret')


def test_user():
    return get_user_model().objects.create_user(**user_args())