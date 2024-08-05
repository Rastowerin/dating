from rest_framework import serializers

from tg_users.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):

    likes = serializers.ReadOnlyField()
    dislikes = serializers.ReadOnlyField()

    class Meta:
        fields = '__all__'
        model = TgUser


class TgUserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TgUser


class TgUserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TgUser


class TgUserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = TgUser
