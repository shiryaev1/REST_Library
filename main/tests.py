from django.test import TestCase

from django.contrib.auth.models import User

from main.models import Book


class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            username='user1',
            first_name='TestName',
            last_name='TestSurname',
            password='123123'
        )
        User.objects.create(
            username='trainer',
            first_name='OtherName',
            last_name='OtherSurname',
            password='qweqwe'
        )
        user1 = User.objects.get(id=1)
        user2 = User.objects.get(id=2)
        Book.objects.create(
            title="Learning Python",
            content="Get a comprehensive, in-depth introduction to the core Python language",
            author="Mark Lutz",
            owner=user1,
        )
        Book.objects.create(
            title="Two Scoops of Django",
            content="Two Scoops of Django: Best Practices For Django",
            owner=user2,
        )

    def test_book_absolute_url(self):
        book1 = Book.objects.get(id=1)
        book2 = Book.objects.get(id=2)
        self.assertEqual(book1.get_absolute_url(), '/book/1/edit/')
        self.assertEqual(book2.get_absolute_url(), '/book/2/edit/')