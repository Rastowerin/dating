from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class APITestCaseWithAuth(APITestCase):

    def setUp(self):

        admin = User.objects.create_user(
            username='admin',
            password='1',
            email='admin@gmail.com',
            is_staff=True,
            is_superuser=True
        )

        self.client.force_authenticate(admin)
        self.client.force_login(admin)

        self.maxDiff = 10**9
