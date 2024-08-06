from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tg_users.models import TgUser
from tg_users.serializers import TgUserSerializer


class TgUserViewSet(ModelViewSet):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer

    def create(self, request, *args, **kwargs):

        super(TgUserViewSet, self).create(request, *args, **kwargs)
        tg_user = TgUser.objects.get(tg_id=request.data['tg_id'])

        headers = self.get_success_headers(request.data)
        return Response(TgUserSerializer(tg_user).data, status=status.HTTP_201_CREATED, headers=headers)
