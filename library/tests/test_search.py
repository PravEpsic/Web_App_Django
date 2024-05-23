from django.test import TestCase, Client
from django.urls import reverse
from library.models import Book

class SearchViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Book.objects.create(title='Test Book', author='Test Author')

    def test_search_view(self):
        response = self.client.get(reverse('search'), {'q': 'Test Book'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        self.assertContains(response, 'Test Author')

    def test_search_view_no_results(self):
        response = self.client.get(reverse('search'), {'q': 'Nonexistent Book'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aucun livre trouvé.')
