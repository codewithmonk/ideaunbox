from urllib import response
from django.urls import reverse
from django.test import SimpleTestCase

class TestHomePage(SimpleTestCase):
    
    def test_homepage_access_using_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_access_using_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)