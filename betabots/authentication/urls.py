from django.conf.urls import include, url
from rest_framework.authtoken import views
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token

urlpatterns = [
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^api-token-auth/', CustomObtainAuthToken.as_view()),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
