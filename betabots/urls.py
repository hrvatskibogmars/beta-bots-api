# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.urls import reverse_lazy
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from users.views import (
    UserViewSet,
    UgovorStrujaViewSet,
    UgovorStrujaListAPIView,
    UgovorLedViewSet,
    HelloPDFView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Ugovor Led', UgovorLedViewSet)
router.register(r'Ugovor Struja', UgovorStrujaViewSet)
router.register(r'Ugovor Struja List', UgovorStrujaListAPIView)


schema_view = get_swagger_view(title='betabots API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^pdf/$', HelloPDFView.as_view()),
    url(r'^$', schema_view),


    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    # url(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
