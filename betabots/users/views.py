from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.generics import ListAPIView



from .models import (
    User,
    UgovorLed,
    UgovorStruja)

from .permissions import IsUserOrReadOnly
from .serializers import (
    CreateUserSerializer,
    UserSerializer,
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


class UgovorStrujaViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = UgovorStruja.objects.all()
    serializer_class = UgovorStrujaSerializer
    permission_classes = (IsUserOrReadOnly,)


class UgovorStrujaListAPIView(viewsets.ModelViewSet):
    queryset = UgovorStruja.objects.all()
    serializer_class = UgovorStrujaSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = UgovorStruja.objects.all()
        oib = self.request.query_params.get('oib', None)
        agent = self.request.query_params.get('oib', None)

        if oib is not None:
            queryset = queryset.filter(oib=oib)
        if agent is not None:
            queryset = queryset.filter(agent=agent)
        return queryset


class UgovorLedViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    queryset = UgovorLed.objects.all()
    serializer_class = UgovorLedSerializer
    permission_classes = (IsUserOrReadOnly,)
