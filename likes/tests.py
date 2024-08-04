import os

from dotenv import load_dotenv
from rest_framework import status

from dating.default_tests_setup import APITestCaseWithAuth
from tg_users.serializers import TgUserCreateSerializer

load_dotenv()
BASE_URl = os.getenv('BASE_URL')


class LikeTests(APITestCaseWithAuth):

    def setUp(self):
        super().setUp()

        sender_data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "location": "59.973871, 30.316447",
            "description": "test_description"
        }

        receiver_data = {
            "tg_id": 148832270,
            "full_name": "Eblan Eblanovich",
            "sex": "FEMALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "location": "59.973871, 30.316447",
            "description": "test_description"
        }

        bad_receiver_data = {
            "tg_id": 148832271,
            "full_name": "Eblan Eblanovich",
            "sex": "FEMALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "location": "59.973871, 30.316447",
            "description": "test_description"
        }

        data_list = [sender_data, receiver_data, bad_receiver_data]

        serializer = TgUserCreateSerializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def test_likes(self):

        data = {
            'sender': 148832269,
            'receiver': 148832270
        }

        response = self.client.post(f'{BASE_URl}/likes/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(f'{BASE_URl}/likes/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {
            'sender': 148832269,
            'receiver': 148832271
        }

        response = self.client.post(f'{BASE_URl}/likes/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
