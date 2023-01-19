from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

class ExampleTestCase(APITestCase):
    def test_invalid_username(self):
        url = reverse('userinfo')
        params = {
            'username' : 'MayurSata'
        }
        response = self.client.get(url,params)
        self.assertTrue(status.is_client_error(response.status_code))

    def test_valid_user_response(self):
        url = reverse('userinfo')
        params = {
            'username' : 'aadityas201'
        }
        response = self.client.get(url,params)
        self.assertTrue(status.is_success(response.status_code))