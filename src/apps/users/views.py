from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.serializers import UserProfileSerializer


class UserProfileApiView(RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        print(self.request.user)
        return get_object_or_404(User, pk=self.request.user.pk)