from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
import json

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.register_url = reverse('start:register')

	def test_register_POST(self):
			
		response = self.client.get(self.register_url)
			
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response,'start/register.html')
			