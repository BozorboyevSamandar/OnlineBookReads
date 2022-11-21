from django.test import TestCase
from django.urls import reverse
from .models import Book


# Create your tests here.


class BookTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))

        self.assertContains(response, "No book found")

    def test_books_list(self):
        Book.objects.create(title="Kitob 1", description="Tarif 1", isbn="1245786595324567")
        Book.objects.create(title="Kitob 2", description="Tarif 2", isbn="1569581981616565")
        Book.objects.create(title="Kitob 3", description="Tarif 3", isbn="8944849465489466")

        response = self.client.get(reverse("books:list"))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_book_detail(self):
        book = Book.objects.create(title="Kitob 1", description="Tarif 1", isbn="1245786595324567")

        response = self.client.get(reverse('books:detail'), kwargs={'id': book.id})

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
