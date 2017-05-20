from rest_framework import serializers

from .models import User, UgovorLed, UgovorStruja


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username', )


class UgovorLedSerializer(serializers.ModelSerializer):

    class Meta:
        model = UgovorLed
        fields = '__all__'


class UgovorStrujaSerializer(serializers.ModelSerializer):

    class Meta:
        model = UgovorStruja
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'auth_token')
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}
