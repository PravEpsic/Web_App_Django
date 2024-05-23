import pytest
from django.urls import reverse, resolve
from library.models import Book
from library.views import book_info

@pytest.fixture
def book(db):
    return Book.objects.create(author="Bastien J", title="450")

def test_book_info_url(book):
    path = reverse("info", args=[str(book.id)])
    assert path == f"/{book.id}"
    resolved_view = resolve(path)
    assert resolved_view.func == book_info
