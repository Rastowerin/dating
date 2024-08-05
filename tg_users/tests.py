import os

from django.core.files.uploadedfile import SimpleUploadedFile
from dotenv import load_dotenv
from rest_framework import status

from dating import settings
from dating.default_tests_setup import APITestCaseWithAuth

load_dotenv()
BASE_URl = os.getenv('BASE_URL', 'http://localhost:8000')


class TestTgUsers(APITestCaseWithAuth):

    def test_create(self):

        image_file = SimpleUploadedFile(
            name='test_files/test.jpg',
            content=b'file_content',
            content_type='image/jpeg'
        )

        data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "ANY",
            "age": 54,
            "city": "Perm`",
            "description": "test",
            "images": [image_file],
        }

        response = self.client.post(f"{BASE_URl}/tg_users/", data=data, files={"images": [image_file]})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(f"{BASE_URl}/tg_users/{data['tg_id']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        excepted = {
            **data,
            "likes": 0,
            "dislikes": 0,
        }

        response_images = response_data.pop("images")

        excepted_images_regex = rf"^{settings.MEDIA_URL}images/*"

        self.assertEqual(len(response_images), 1)
        self.assertRegex(response_images[0]["image"], excepted_images_regex)

        self.assertDictEqual(response_data, excepted)
