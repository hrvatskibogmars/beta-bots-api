from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import (
    User,
    Korisnik,
    UgovorLed,
    UgovorStruja)

from .permissions import IsUserOrReadOnly
from .serializers import (
    CreateUserSerializer,
    UserSerializer,
    KorisnikSerializer,
    UgovorLedSerializer,
    UgovorStrujaSerializer)


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)


class KorisnikViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer


class UgovorStrujaViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
        """
        Creates, Updates, and retrives User accounts
        """
        queryset = UgovorStruja.objects.all()
        serializer_class = UgovorStrujaSerializer


class UgovorLedViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = UgovorLed.objects.all()
    serializer_class = UgovorLedSerializer
