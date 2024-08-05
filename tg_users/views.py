from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from tg_users.models import TgUser
from tg_users.serializers import TgUserSerializer, TgUserCreateSerializer


class TgUserViewSet(ModelViewSet):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer_class = TgUserCreateSerializer
        return super(TgUserViewSet, self).create(request, *args, **kwargs)
