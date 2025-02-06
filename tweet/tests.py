from django.test import TestCase
from django.urls import reverse

class SimpleTestCase(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('tweet_edit'))  
        self.assertEqual(response.status_code, 200)

