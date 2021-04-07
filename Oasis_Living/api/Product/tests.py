from django.test import TestCase

# Create your tests here.
import json

from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase


class EndPointsTestcase(APITestCase):

    def test_endpoint(self):
        data = {
            "SKU": "9283",
            "Name": "Apple iPhone 7",
            "Qty": 8,
            "Price": "22.23"
        }
        response = self.client.post(
            "/api/products/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
