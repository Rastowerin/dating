from django.core.files.uploadedfile import SimpleUploadedFile

from dating import settings
from dating.default_tests_setup import APITestCaseWithAuth
from tg_users.models import TgUser, TgUserImage


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

        tg_user = TgUser.objects.create(**data)
        tg_user.save()

        image_file = SimpleUploadedFile(
            name='test_files/test.jpg',
            content=b'file_content',
            content_type='image/jpeg'
        )

        image_data = {
            "id": 1,
            "image": image_file
        }

        TgUserImage(**image_data, tg_user=tg_user).save()

        response = self.client.get(f"http://127.0.0.1:8000/tg_users/{tg_user.tg_id}/")
        response_data = response.json()

        self.assertEqual(response.status_code, 200)

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
