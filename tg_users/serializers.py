from drf_extra_fields.fields import Base64ImageField
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from tg_users.models import TgUser, TgUserImage


class TgUserImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        fields = ['image']
        model = TgUserImage


class TgUserSerializer(WritableNestedModelSerializer):

    images = TgUserImageSerializer(many=True, required=False)
    likes = serializers.ReadOnlyField()
    dislikes = serializers.ReadOnlyField()

    class Meta:
        fields = '__all__'
        model = TgUser
