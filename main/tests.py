from django.test import TestCase

from django.contrib.auth.models import User

from main.models import Book


class MainTestCase(TestCase):
    def test_setUp(self):
        user1 = User.objects.create(
            username='user1',
            first_name='TestName',
            last_name='TestSurname',
            password='123123'
        )
        user2 = User.objects.create(
            username='trainer',
            first_name='OtherName',
            last_name='OtherSurname',
            password='qweqwe'
        )
        return user1, user2

    def test_book_create(self):
        user1, user2 = self.test_setUp()
        book1 = Book.objects.create(
            title="Learning Python",
            content="Get a comprehensive, in-depth introduction to the core Python language",
            author="Mark Lutz",
            owner=user1,
        )
        book2 = Book.objects.create(
            title="Two Scoops of Django",
            content="Two Scoops of Django: Best Practices For Django",
            author="Lutz",
            owner=user2,
        )

        return book1, book2

    def test_book_absolute_url(self):
        book1, book2 = self.test_book_create()
        self.assertEqual(book1.get_absolute_url(), f'/book/{book1.id}/edit/')
        self.assertEqual(book2.get_absolute_url(), f'/book/{book2.id}/edit/')
