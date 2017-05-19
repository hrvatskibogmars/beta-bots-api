from django.conf.urls import include, url
from rest_framework.authtoken import views
from .views import CustomObtainAuthToken

urlpatterns = [
    # url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-token-auth/', CustomObtainAuthToken.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
