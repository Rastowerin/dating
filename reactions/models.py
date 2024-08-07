from django.db import models
from django.db.models.manager import Manager

from tg_users.models import TgUser


class ReactionsManager(Manager):

    def check_opposite_reaction_exists(self, reaction):
        return self.filter(sender=reaction.receiver, receiver=reaction.sender, type=reaction.type).exists()


class Reaction(models.Model):

    class Types(models.TextChoices):
        LIKE = ('LIKE', 'like')
        DISLIKE = ('DISLIKE', 'dislike')

    sender = models.ForeignKey(TgUser, related_name='sent_reactions', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(TgUser, related_name='received_reactions', on_delete=models.DO_NOTHING)
    type = models.CharField(choices=Types.choices)
    sent_at = models.DateTimeField(auto_now_add=True)

    objects = ReactionsManager()
