from rest_framework import routers

from .views import UserViewSet

urlpatterns = []

router = routers.DefaultRouter()

router.register('', UserViewSet)

urlpatterns += router.urls
