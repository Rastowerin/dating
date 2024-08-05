from rest_framework import serializers

from tg_users.models import TgUser, TgUserImage


class TgUserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUserImage
        fields = ['image']


class TgUserSerializer(serializers.ModelSerializer):

    images = TgUserImageSerializer(many=True, required=False)
    likes = serializers.ReadOnlyField()
    dislikes = serializers.ReadOnlyField()

    class Meta:
        fields = '__all__'
        model = TgUser

    def create(self, validated_data):

        if 'images' not in validated_data:
            return super().create(validated_data)

        images_data = validated_data.pop('images')
        tg_user = TgUser.objects.create(**validated_data)

        for image_data in images_data:
            image = TgUserImage.objects.create(tg_user=tg_user, **image_data)
            tg_user.images.add(image)

        return tg_user
