from django.urls import path
from rest_framework import routers

from .views import ListUsers

urlpatterns = [path('search/<int:tg_id>/', ListUsers.as_view(), name='list-tg_users')]
