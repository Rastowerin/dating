from rest_framework import routers

from .views import TgUserViewSet

urlpatterns = []

router = routers.DefaultRouter()

router.register('', TgUserViewSet)

urlpatterns += router.urls
