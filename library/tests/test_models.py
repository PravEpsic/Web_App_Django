import pytest
from library.models import Book

@pytest.fixture
def book(db):
    return Book.objects.create(author='Author Name', title='Book Title')

def test_author_label(book):
    field_label = book._meta.get_field('author').verbose_name
    assert field_label == 'author'

def test_title_label(book):
    field_label = book._meta.get_field('title').verbose_name
    assert field_label == 'title'

def test_author_max_length(book):
    max_length = book._meta.get_field('author').max_length
    assert max_length == 50

def test_title_max_length(book):
    max_length = book._meta.get_field('title').max_length
    assert max_length == 50

def test_object_name_is_author_title(book):
    expected_object_name = f'{book.author} | {book.title}'
    assert expected_object_name == str(book)
