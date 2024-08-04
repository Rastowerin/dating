from django.db import models
from django.db.models.manager import Manager
from rest_framework.exceptions import ValidationError

from tg_users.models import TgUser


class LikeManager(Manager):

    def check_opposite_like_exists(self, like):
        return self.filter(sender=like.receiver, receiver=like.sender).exists()


class Like(models.Model):

    sender = models.ForeignKey(TgUser, related_name='sent_likes', on_delete=models.CASCADE)
    receiver = models.ForeignKey(TgUser, related_name='received_likes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    objects = LikeManager()
