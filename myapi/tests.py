from django.test import TestCase


class MyAPITest(TestCase):
    def test_get_first_page_by_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_get_movies_by_url(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)