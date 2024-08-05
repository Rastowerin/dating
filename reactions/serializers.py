from datetime import timedelta

from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from reactions.models import Reaction
from tg_users.models import TgUser


class ReactionReadSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Reaction


class ReactionCreateSerializer(ModelSerializer):

    def validate(self, attrs):

        if not TgUser.objects.check_preferences_matches(tg_user1=attrs['sender'], tg_user2=attrs['receiver']):

            raise serializers.ValidationError("Users preferences do not match")

        one_week_ago = timezone.now() - timedelta(days=7)

        if Reaction.objects.filter(
                sender=attrs['sender'],
                receiver=attrs['receiver'],
                type=attrs['type'],
                sent_at__gte=one_week_ago
        ).exists():

            raise serializers.ValidationError("Reaction already exists")

        return attrs

    class Meta:
        exclude = ['sent_at']
        model = Reaction
