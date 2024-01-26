from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserRegistrationSerializer, UserCreateSerializer as BaseUserCreateSerializer

from StoreFront.store.models import Customer

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name')