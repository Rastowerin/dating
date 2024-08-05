from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from reactions.serializers import ReactionCreateSerializer


class CreateReactions(CreateAPIView):
    serializer_class = ReactionCreateSerializer
    permission_classes = [IsAdminUser]
