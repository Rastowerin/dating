import os

from dotenv import load_dotenv
from rest_framework import status

from dating.default_tests_setup import APITestCaseWithAuth

load_dotenv()
BASE_URl = os.getenv('BASE_URL', 'http://localhost:8000')


class TestTgUsers(APITestCaseWithAuth):

    def test_create(self):

        data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "ANY",
            "age": 54,
            "city": "Perm`",
            "description": "test",
        }

        response = self.client.post(f"{BASE_URl}/tg_users/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(f"{BASE_URl}/tg_users/{data['tg_id']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        excepted = {
            **data,
            "likes": 0,
            "dislikes": 0,
            "images": [],
        }

        self.assertDictEqual(response_data, excepted)
