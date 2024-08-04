from django.urls import path

from .views import CreateLikes

urlpatterns = [path('likes/', CreateLikes.as_view(), name='create-likes')]
