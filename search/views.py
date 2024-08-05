from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter

from tg_users.models import TgUser
from tg_users.serializers import TgUserSerializer
from search.algorithm import search_algorithm


class SearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommonListTgUsers(ListAPIView):

    serializer_class = TgUserSerializer
    permission_classes = [IsAdminUser]
    pagination_class = SearchPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['age']


class ListRecommendedTgUsers(CommonListTgUsers):

    def get(self, request, tg_id, *args, **kwargs):

        tg_user = TgUser.objects.get(tg_id=tg_id)
        self.queryset = search_algorithm(tg_user)

        return super().get(request, *args, **kwargs)


class ListLikedTgUsers(CommonListTgUsers):

    def get(self, request, tg_id, *args, **kwargs):

        self.queryset = TgUser.objects.filter(sent_reactions__receiver__tg_id=tg_id, sent_reactions__type='LIKE')

        return super().get(request, *args, **kwargs)
