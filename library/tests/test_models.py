from django.test import TestCase
from library.models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Book.objects.create(author='Author Name', title='Book Title')

    def test_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')  # Modifiez cette ligne

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')  # Modifiez cette ligne

    def test_author_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author').max_length
        self.assertEqual(max_length, 50)  # Modifiez cette ligne

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)  # Modifiez cette ligne

    def test_object_name_is_author_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.author} | {book.title}'
        self.assertEqual(expected_object_name, str(book))  # Modifiez cette ligne
