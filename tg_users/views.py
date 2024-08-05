from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
import requests

from tg_users.models import TgUser, TgUserImage
from tg_users.serializers import TgUserSerializer


class TgUserViewSet(ModelViewSet):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):

        super(TgUserViewSet, self).create(request, *args, **kwargs)
        tg_user = TgUser.objects.get(tg_id=request.data['tg_id'])

        images = request.data['images']

        for image_url in images:

            image_bytes = requests.get(image_url).content
            image = SimpleUploadedFile("image", image_bytes, content_type='image/jpeg')
            TgUserImage.objects.create(tg_user=tg_user, image=image)

        headers = self.get_success_headers(request.data)
        return Response(TgUserSerializer(tg_user).data, status=status.HTTP_201_CREATED, headers=headers)
