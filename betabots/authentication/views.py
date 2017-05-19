from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# from ..users.models import User


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        # token = Token.objects.get(key=response.data['token'])
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        # user_info = User.objects.get(user=user)
        # return Response({'token': token.key})
        full_name = "{} {}".format(user.first_name, user.last_name)

        return Response({'token': token.key,
                         'role': user.role,
                         'name': full_name
                         })
