from rest_framework.viewsets import ModelViewSet

from reactions.models import Reaction
from reactions.serializers import ReactionSerializer


class ReactionViewSet(ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
