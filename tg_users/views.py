from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from tg_users.models import TgUser
from tg_users.serializers import TgUserSerializer


class TgUserViewSet(ModelViewSet):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer
    permission_classes = [IsAdminUser]
