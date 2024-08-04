from django.urls import path

from .views import ListRecommendedTgUsers, ListLikedTgUsers

urlpatterns = [
    path('recommended/<int:tg_id>/', ListRecommendedTgUsers.as_view(), name='list-recommended-tg_users'),
    path('liked/<int:tg_id>/', ListLikedTgUsers.as_view(), name='list-liked-tg_users'),
]
