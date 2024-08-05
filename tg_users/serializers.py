from rest_framework import serializers

from tg_users.models import TgUser, TgUserImage


class TgUserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUserImage
        fields = ['image']


class TgUserSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()
    likes = serializers.ReadOnlyField()
    dislikes = serializers.ReadOnlyField()

    def get_images(self, obj):
        return list(map(lambda image: str(image), obj.images.all()))

    class Meta:
        fields = '__all__'
        model = TgUser
