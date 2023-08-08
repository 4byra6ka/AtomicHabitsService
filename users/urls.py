from rest_framework.routers import DefaultRouter
from users.views import UsersCreateView, UsersListView, UsersDetailView, UsersUpdateView, UsersDeleteView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path("registration/", UsersCreateView.as_view(), name='registration'),
    path("", UsersListView.as_view(), name='users_list'),
    path("<str:username>/", UsersDetailView.as_view(), name='users_detail'),
    path("<str:username>/", UsersUpdateView.as_view(), name='users_update'),
    path("<str:username>/", UsersDeleteView.as_view(), name='users_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]