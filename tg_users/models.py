from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy


class TgUserManager(Manager):

    @staticmethod
    def check_preferences_matches(tg_user1, tg_user2):
        other_sex = {
            'MALE': 'FEMALE',
            'FEMALE': 'MALE'
        }[tg_user1.sex]

        not_preferred_sex = {
            'MALE': 'FEMALE',
            'FEMALE': 'MALE',
            'ANY': None
        }[tg_user1.sex_preference]

        return tg_user2.sex != not_preferred_sex and tg_user2.sex_preference != other_sex


class TgUser(models.Model):
    class Sex(models.TextChoices):
        MALE = 'MALE', gettext_lazy('Male')
        FEMALE = 'FEMALE', gettext_lazy('Female')

    class SexPreference(models.TextChoices):
        MALE = 'MALE', gettext_lazy('Male')
        FEMALE = 'FEMALE', gettext_lazy('Female')
        ANY = 'ANY', gettext_lazy('Any')

    tg_id = models.IntegerField(unique=True, primary_key=True)
    full_name = models.CharField(max_length=255, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    sex = models.CharField(max_length=50, blank=False, null=False, choices=Sex.choices)
    sex_preference = models.CharField(max_length=50, blank=False, null=False, choices=SexPreference.choices)
    description = models.TextField(blank=False, null=False)

    @property
    def likes(self):
        return self.received_reactions.filter(type='LIKE').count()

    @property
    def dislikes(self):
        return self.received_reactions.filter(type='DISLIKE').count()

    objects = TgUserManager()

    def __str__(self):
        return self.full_name


class TgUserImage(models.Model):
    tg_user = models.ForeignKey(TgUser, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.tg_user}"
