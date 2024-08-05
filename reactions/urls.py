from django.urls import path

from .views import CreateReactions

urlpatterns = [path('reactions/', CreateReactions.as_view(), name='create-reactions')]
