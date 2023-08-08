from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'tg_user_id', 'first_name', 'last_name', 'is_active',)


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    description = serializers.SerializerMethodField(read_only=True)
    # class Meta:
    #     model = User
    #     fields = 'username'

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            is_active=False
        )
        user.save()

    def get_description(self, instance):
        return '!!!Учетная запись созданна вам нужно активировать её через телеграм бот нажатием /start!!!'