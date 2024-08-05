
from django.contrib.auth.models import User
from dating.default_tests_setup import APITestCaseWithAuth
from tg_users.models import TgUser
from tg_users.serializers import TgUserCreateSerializer


class TestTgUsers(APITestCaseWithAuth):

    def test_create(self):

        data = {
            "tg_id": 148832269,
            "full_name": "Eblan Eblanovich",
            "sex": "MALE",
            "sex_preference": "ANY",
            "age": 54,
            "city": "Perm`",
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
                           "зоро гошы вама каке неро пото рожа родо лое шогу мира подо жоло"
        }

        tg_user = TgUser.objects.create(**data)
        tg_user.save()

        response = self.client.get(f"http://127.0.0.1:8000/tg_users/{tg_user.tg_id}/")

        self.assertEqual(response.status_code, 200)

        excepted = {
            **data,
            "likes": 0,
            "dislikes": 0,
        }

        self.assertDictEqual(dict(response.data), excepted)
