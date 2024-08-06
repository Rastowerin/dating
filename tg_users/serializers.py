import base64

import requests
from django.core.files.uploadedfile import SimpleUploadedFile
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

    def save(self, **kwargs):

        if 'images' not in self.initial_data.keys():
            return super().save(**kwargs)

        images = self.initial_data['images']

        instance = super().save(**kwargs)
        instance.images.all().delete()

        for image_url in images:

            image_data = base64.b64decode(image_url.split(',')[1])
            image = SimpleUploadedFile("image", image_data, content_type='image/jpeg')

            TgUserImage.objects.create(tg_user=instance, image=image)

        return instance

    class Meta:
        fields = '__all__'
        model = TgUser
