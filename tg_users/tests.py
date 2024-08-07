import os

from dotenv import load_dotenv
from rest_framework import status

from dating.default_tests_setup import APITestCaseWithAuth

load_dotenv()
BASE_URl = os.getenv('BASE_URL', 'http://localhost:8000')


class TestTgUsers(APITestCaseWithAuth):

    def test_create(self):
        image_base64 = open('test_files//img_url.txt', 'r').read()

        data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "ANY",
            "age": 54,
            "city": "Perm`",
            "description": "test",
            "images": [
                {
                    "image": image_base64,
                },
            ],
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
            "videos": []
        }
        del excepted["images"]

        self.assertTrue("images" in response_data)
        images = response_data.pop("images")
        self.assertEqual(len(images), len(data["images"]))

        for image_url in images:
            self.assertTrue(image_url['image'].startswith(
                "https://storage.yandexcloud.net/dating-bot/images/"
            ))

        self.assertDictEqual(response_data, excepted)
