from django.test import TestCase, Client
from unittest.mock import patch
from library.models import Book
from library.views import index

class IndexViewTest(TestCase):
    @patch('library.views.Book.objects.all')
    def test_index_view(self, mock_books):
        # Créer un client
        client = Client()

        # Créer un mock pour les livres
        mock_books.return_value.count.return_value = 10

        # Appeler la vue index
        response = client.get('/')

        # Vérifier que la vue a renvoyé le bon nombre de livres
        self.assertEqual(response.context['num_books'], 10)
