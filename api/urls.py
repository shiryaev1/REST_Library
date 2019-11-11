from django.urls import path

from api.views import UserListAPIView

app_name = 'api'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
]