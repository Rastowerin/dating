
from django.contrib.auth.models import User

from dating.default_tests_setup import APITestCaseWithAuth
from tg_users.models import TgUser
from tg_users.serializers import TgUserCreateSerializer


class TestTgUsers(APITestCaseWithAuth):

    def test_create(self):

        self_data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "location": "59.973871, 30.316447",
            "description": "test_description"
        }

        recommended_user_data = {
            "tg_id": 148832212,
            "full_name": "Eblan Eblanovich 2",
            "sex": "FEMALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "location": "59.973871, 30.316447",
            "description": "test_description"
        }

        not_recommended_user_data1 = {
            "tg_id": 148832133,
            "full_name": "Eblan Eblanovich 3",
            "sex": "MALE",
            "sex_preference": "MALE",
            "age": 54,
            "city": "Perm`",
            "location": "59.973871, 30.316447",
            "description": "test_description"
        }

        not_recommended_user_data2 = {
            "tg_id": 148832356,
            "full_name": "Eblan Eblanovich 4",
            "sex": "FEMALE",
            "sex_preference": "FEMALE",
            "age": 54,
            "city": "Perm`",
            "location": "59.973871, 30.316447",
            "description": "test_description"
        }

        data_list = [self_data, recommended_user_data, not_recommended_user_data1, not_recommended_user_data2]

        serializer = TgUserCreateSerializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = self.client.get(f"http://127.0.0.1:8000/search/{self_data['tg_id']}?ordering=age", follow=True)

        self.assertEqual(response.status_code, 200)

        results = response.json()['results']

        excepted = [
            {
                **recommended_user_data
            },
        ]

        self.assertEqual(len(results), 1)
        self.assertDictEqual(results[0], excepted[0])
