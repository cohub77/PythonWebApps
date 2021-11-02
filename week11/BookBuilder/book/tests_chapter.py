from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Author, Book, Chapter
from .tests_author import create_test_user


class ChapterDataTest(TestCase):

    def setUp(self):
        self.user, self.user_args = create_test_user()

        # self.user = create_test_user()
        self.author1 = Author.objects.create(user=self.user, name='Chuck Dickens')
        self.author2 = Author.objects.create(user=self.user, name='Homer')
        self.book1 = Book.objects.create(title='Tale of 2 Cities', author=self.author1,
                                         description='None', doc_path='Documents')
        self.book2 = Book.objects.create(title='Iliad', author=self.author2,
                                         description='None', doc_path='Documents')

        self.chapter1 = dict(book=self.book2, title='Achilles', order='1', document='1.md')
        self.chapter2 = dict(book=self.book2, title='Agamememnon', order='2', document='2.md')

    def test_add_chapter(self):
        self.assertEqual(len(Chapter.objects.all()), 0)
        Chapter.objects.create(**self.chapter1)
        Chapter.objects.create(**self.chapter2)
        self.assertEqual(len(Chapter.objects.all()), 2)

    def test_chapter_list(self):
        Chapter.objects.create(**self.chapter1)
        Chapter.objects.create(**self.chapter2)
        b = Chapter.objects.filter(book=self.book2).order_by('order')
        self.assertEqual(b[0].title, 'Achilles')
        self.assertEqual(b[1].title, 'Agamememnon')
        self.assertEqual(b[1].document, '2.md')

    def test_chapter_edit(self):
        Chapter.objects.create(**self.chapter1)
        b = Chapter.objects.get(pk=1)
        b.title = 'Agamememnon'
        b.order = 2
        b.document = '2.md'
        b.save()
        self.assertEqual(b.title, 'Agamememnon')
        self.assertEqual(b.order, 2)
        self.assertEqual(b.document, '2.md')

    def test_chapter_delete(self):
        Chapter.objects.create(**self.chapter1)
        b = Chapter.objects.get(pk=1)
        b.delete()
        self.assertEqual(len(Chapter.objects.all()), 0)


class ChapterViewsTest(TestCase):

    def login(self):
        response = self.client.login(username=self.user.username,  password=self.user_args['password'])
        self.assertEqual(response, True)

    def setUp(self):
        self.user, self.user_args = create_test_user()

        self.author = Author.objects.create(user=self.user, name='Charles Dickens')
        self.book = Book.objects.create(title='Tale of Two Cities', author=self.author,
                                        description='description', doc_path='Documents')
        self.chapter1 = dict(book=self.book, title='Best of Times',
                             order='1', html='x', markdown='x', document='1.md')
        self.chapter2 = dict(book=self.book, title='Worst of Times',
                             order='2', html='x', markdown='x', document='2.md')

    def test_chapter_list_view(self):
        Chapter.objects.create(**self.chapter1)
        self.assertEqual(reverse('chapter_list'), '/chapter/')
        response = self.client.get('/chapter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chapter_list.html')
        self.assertTemplateUsed(response, 'theme.html')
        self.assertContains(response, '<tr>', count=2)

    def test_chapter_detail_view(self):
        self.assertEqual(reverse('chapter_detail', args='1'), '/chapter/1')
        self.assertEqual(reverse('chapter_detail', args='2'), '/chapter/2')
        Chapter.objects.create(**self.chapter1)
        response = self.client.get(reverse('chapter_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_chapter_add_view(self):

        # Add without Login
        response = self.client.post(reverse('chapter_add'), self.chapter1)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/add')

        # Login to add
        self.login()
        response = self.client.post(reverse('chapter_add'), self.chapter1)
        response = self.client.post(reverse('chapter_add'), self.chapter2)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/chapter/')

        # List the chapters
        response = self.client.get('/chapter/')
        self.assertContains(response, '<tr>', count=3)

    def test_chapter_edit_view(self):

        # Edit without Login
        self.assertEqual(reverse('chapter_edit', args='1'), '/chapter/1/')
        response = self.client.get('/chapter/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/chapter/1/')

        # Login to edit
        self.login()
        # chapter = dict(title='Worst of Times', order='2', html='x', markdown='x', document='2.md')
        # Chapter.objects.create(**chapter)
        response = self.client.get('/chapter/1')
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Best of Times')

        # # Check after edit
        # response = self.client.post('/chapter/1/', self.chapter2)
        # response = self.client.get('/chapter/1')
        # self.assertContains(response, 'Agamememnon')
        # self.assertContains(response, '2.md')

        response = self.client.get('/chapter/1/')
        self.assertEqual(response.status_code, 302)

        response = self.client.post('/chapter/1/', self.chapter2)
        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.url, '/chapter/')
        # response = self.client.get(response.url)
        # self.assertContains(response, self.book2['title'])
        # self.assertContains(response, self.author1.name)

        # # Check the book object
        # book = Book.objects.get(pk=1)
        # self.assertEqual(book.author, self.author1)
        # self.assertEqual(book.title, 'Odyssey')

#     def test_chapter_delete_view(self):
#         self.login()
#         Chapter.objects.create(**self.chapter1)
#         self.assertEqual(reverse('chapter_delete', args='1'), '/chapter/1/delete')
#         response = self.client.get('/chapter/1/delete')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/chapter/1/delete')
#         self.assertEqual(len(Chapter.objects.all()), 0)
