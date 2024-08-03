from rest_framework import serializers

from tg_users.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TgUser


class TgUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['likes', 'dislikes']
        model = TgUser


class TgUserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['tg_id', 'likes', 'dislikes']
        model = TgUser


class TgUserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['likes', 'dislikes']
        model = TgUser
