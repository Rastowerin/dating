from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from likes.models import Like
from tg_users.models import TgUser


class LikeReadSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Like


class LikeCreateSerializer(ModelSerializer):

    def validate(self, attrs):

        if not TgUser.objects.check_preferences_matches(tg_user1=attrs['sender'], tg_user2=attrs['receiver']):
            raise serializers.ValidationError("Users preferences do not match")

        if Like.objects.filter(sender=attrs['sender'], receiver=attrs['receiver']).exists():
            raise serializers.ValidationError("Like already exists")

        return attrs

    class Meta:
        exclude = ['date']
        model = Like
