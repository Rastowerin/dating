from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from likes.serializers import LikeCreateSerializer


class CreateLikes(CreateAPIView):

    serializer_class = LikeCreateSerializer
    permission_classes = [IsAdminUser]
