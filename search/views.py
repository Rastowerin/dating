from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from tg_users.models import TgUser
from tg_users.serializers import TgUserSerializer
from search.algorithm import search_algorithm


class SearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


def common_search(request, queryset):

    ordering = request.query_params.get('ordering', None)
    if ordering:
        queryset = queryset.order_by(ordering)

    paginator = SearchPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    serializer = TgUserSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def recommended(request, tg_id):
    tg_user = TgUser.objects.get(tg_id=tg_id)
    queryset = search_algorithm(tg_user)
    return common_search(request, queryset)


@api_view(['GET'])
def liked(request, tg_id):
    queryset = TgUser.objects.filter(sent_reactions__receiver__tg_id=tg_id, sent_reactions__type='LIKE')
    return common_search(request, queryset)
