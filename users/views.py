from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsModerator, IsOwner
from users.serializers import UserSerializer, UserCreateSerializer


class UsersCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsModerator]


class UsersDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UsersDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'
