from django.urls import path, re_path

from api.views import UserListAPIView, UserBookLibAPIView, BookUpdateAPIView

app_name = 'api'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    re_path('^lib/(?P<id>\d+)/$', UserBookLibAPIView.as_view(), name='user-lib'),
    re_path('^book/(?P<id>\d+)/edit/$', BookUpdateAPIView.as_view(), name='book-edit'),
]