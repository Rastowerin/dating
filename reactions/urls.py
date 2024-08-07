from rest_framework.routers import DefaultRouter

from .views import ReactionViewSet

router = DefaultRouter()
router.register('', ReactionViewSet, basename='Reaction')

urlpatterns = [
    *router.urls,
]
