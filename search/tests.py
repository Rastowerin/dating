import os

from dotenv import load_dotenv
from rest_framework import status

from dating.default_tests_setup import APITestCaseWithAuth
from reactions.models import Reaction
from tg_users.models import TgUser

load_dotenv()
BASE_URl = os.getenv('BASE_URL')


class TestTgUsers(APITestCaseWithAuth):

    def test_recommended(self):

        self_data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        recommended_user_data = {
            "tg_id": 148832212,
            "full_name": "Eblan Eblanovich 2",
            "sex": "FEMALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        disliked_user_data = {
            "tg_id": 1488321323,
            "full_name": "Eblan Eblanovich 123",
            "sex": "FEMALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        not_recommended_user_data1 = {
            "tg_id": 148832133,
            "full_name": "Eblan Eblanovich 3",
            "sex": "MALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        not_recommended_user_data2 = {
            "tg_id": 148832356,
            "full_name": "Eblan Eblanovich 4",
            "sex": "FEMALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        user_sent_like_data = {
            "tg_id": 148833135,
            "full_name": "Eblan Eblanovich 4",
            "sex": "FEMALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        data_list = [
            self_data,
            recommended_user_data,
            disliked_user_data,
            not_recommended_user_data1,
            not_recommended_user_data2,
            user_sent_like_data,
        ]

        list(map(lambda data: TgUser.objects.create(**data), data_list))

        Reaction.objects.create(
            sender=TgUser(**user_sent_like_data),
            receiver=TgUser(**self_data),
            type='LIKE'
        )

        Reaction.objects.create(
            sender=TgUser(**self_data),
            receiver=TgUser(**disliked_user_data),
            type='DISLIKE'
        )

        response = self.client.get(f"{BASE_URl}/search/recommended/{self_data['tg_id']}?ordering=age", follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.json()['results']

        excepted = [
            {
                **recommended_user_data,
                'likes': 0,
                'dislikes': 0,
                'images': []
            },
        ]

        self.assertEqual(len(results), 1)
        self.assertDictEqual(results[0], excepted[0])

    def test_liked(self):

        self_data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        user_sent_like_data = {
            "tg_id": 148833135,
            "full_name": "Eblan Eblanovich 4",
            "sex": "FEMALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "description": "test_description"
        }

        data_list = [
            self_data,
            user_sent_like_data,
        ]

        list(map(lambda data: TgUser.objects.create(**data), data_list))

        Reaction.objects.create(
            sender=TgUser(**user_sent_like_data),
            receiver=TgUser(**self_data),
            type='LIKE'
        )

        response = self.client.get(f"{BASE_URl}/search/liked/{self_data['tg_id']}?ordering=age", follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        results = response.json()['results']

        excepted = [
            {
                **user_sent_like_data,
                'likes': 0,
                'dislikes': 0,
                'images': []
            },
        ]

        self.assertEqual(len(results), 1)
        self.assertDictEqual(results[0], excepted[0])
