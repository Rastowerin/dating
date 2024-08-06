from django.urls import path
from .views import recommended, liked

urlpatterns = [
    path('recommended/<int:tg_id>/', recommended, name='recommended'),
    path('liked/<int:tg_id>/', liked, name='liked'),
]
