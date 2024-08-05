import os

from dotenv import load_dotenv
from rest_framework import status

from dating.default_tests_setup import APITestCaseWithAuth
from tg_users.serializers import TgUserSerializer

load_dotenv()
BASE_URl = os.getenv('BASE_URL')


class LikeTests(APITestCaseWithAuth):

    def setUp(self):
        super().setUp()

        self.sender_data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        self.receiver_data = {
            "tg_id": 148832270,
            "full_name": "Eblan Eblanovich",
            "sex": "FEMALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        self.bad_receiver_data = {
            "tg_id": 148832271,
            "full_name": "Eblan Eblanovich",
            "sex": "FEMALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        data_list = [self.sender_data, self.receiver_data, self.bad_receiver_data]

        serializer = TgUserSerializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def test_likes(self):

        data = {
            'sender': self.sender_data['tg_id'],
            'receiver': self.receiver_data['tg_id'],
            'type': 'LIKE'
        }

        response = self.client.post(f'{BASE_URl}/reactions/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(f'{BASE_URl}/reactions/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], 'Reaction already exists')

        data = {
            'sender': self.sender_data['tg_id'],
            'receiver': self.bad_receiver_data['tg_id'],
            'type': 'LIKE'
        }

        response = self.client.post(f'{BASE_URl}/reactions/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], 'Users preferences do not match')
