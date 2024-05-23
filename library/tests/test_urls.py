import pytest
from django.urls import reverse, resolve
from library.models import Book
from library.views import book_info

@pytest.mark.django_db
def test_book_info_url():
    # Create a book using the Book model + DB save
    book = Book.objects.create(author="Bastien J", title="450")
    path = reverse("info", args=[str(book.id)])

    # Check if the URL is correct
    assert path == f"/{book.id}"

    # Check if the URL resolves to the correct view function
    resolved_view = resolve(path)
    assert resolved_view.func == book_info
