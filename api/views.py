from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import UserListCreateSerializer


class UserListAPIView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserListCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        users = User.objects.all()
        serializer = UserListCreateSerializer(users, many=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)