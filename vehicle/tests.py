from rest_framework import status
from rest_framework.test import APITestCase


class VehicleTestCase(APITestCase):
   def setUp(self) -> None:
       pass

   def test_create_car(self):
       """тестирование создания машины"""
       data = {
           'title': 'Test',
           'description': 'Test'
       }

       response = self.client.post(
           '/cars/',
           data=data
       )

       self.assertEqual(
           response.status_code,
           status.HTTP_201_CREATED
       )