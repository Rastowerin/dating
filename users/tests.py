from datetime import datetime

from rest_framework.test import APITestCase

from users.models import User


class TestUser(APITestCase):

    def setUp(self):

        admin = User.objects.create_user(username='admin', password='1', email='admin@gmail.com', is_staff=True, is_superuser=True)

        self.client.force_authenticate(admin)
        self.client.force_login(admin)

        self.maxDiff = 10**9

    def test_create(self):

        data = {"tg_id": 148832269,
                "full_name": "Eblan Eblanovich",
                "username": "12345",
                "email": "12345",
                "password": "1",
                "sex": "Male",
                "age": 54,
                "city": "Perm`",
                "location": "59.973871, 30.316447",
                "description": "Я тебя ебал гад срать на нас говна. Я тебя ебал гадить нас срать"
                               " так. Я тега егал могол срать на нас говда. Я тега егад могол сдат"
                               " над мого. Я тега ега мого така мого. я тага мого така водо мога."
                               " я тега пото мога подо роды мого пира тора, я мого тара пото раво"
                               " года мого мара мира бора пото доро нора това кара его хора пото"
                               " шоря часа вода пото мира его ура поты жора пото мира его шоры"
                               " вадо ига пото дора пото боры вадо году щора пото его ура поро "
                               "ено гора пото ира поты дора тора позо кара ура пого ыра нога мита "
                               "побо лота дора жого тора пото мога побо рода поло шора кога его "
                               "нора пото часы жоло гоша кепо роты вады кана гора пото мира пото "
                               "рада шора дора пото мира аго кара его щора пото кера пото гора "
                               "перо его жоло рода пото рада его шора пото его неро рода ено гора"
                               " щора щора перо керо вадо лоша пора мого куне кего зоро голо аво "
                               "зоро гошы вама каке неро пото рожа родо лое шогу мира подо жоло"}

        user = User.objects.create(**data)

        response = self.client.get(f"http://127.0.0.1:8000/users/{user.pk}/")

        self.assertEqual(response.status_code, 200)

        excepted = {
            **data,
            "id": 2,
        }

        del excepted["password"]

        self.assertDictEqual(dict(response.data), excepted)
