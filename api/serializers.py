from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
)

from main.models import Book


class UserListCreateSerializer(ModelSerializer):

    library = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
            'library',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def get_library(self, obj):
        return f'/api/lib/{obj.id}/'


class BookListCreateSerializer(ModelSerializer):
    owner = CharField(read_only=True)
    edit_url = SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id',
            'owner',
            'title',
            'content',
            'author',
            'edit_url',
        ]
        extra_kwargs = {
            "owner": {
                "read_only": True
            }
        }

    def get_edit_url(self, obj):
        return f'/api/book/{obj.id}/edit/'


class BookDetailSerializer(ModelSerializer):
    owner = CharField(read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'owner',
            'title',
            'content',
            'author',
        ]
        extra_kwargs = {
            "owner": {
                "read_only": True
            }
        }