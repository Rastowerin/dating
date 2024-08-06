from rest_framework import routers

from .views import TgUserViewSet

router = routers.DefaultRouter()

router.register('', TgUserViewSet, basename='TgUser')

urlpatterns = [
    *router.urls,
]
