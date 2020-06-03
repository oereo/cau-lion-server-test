from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from accounts.views import CustomRegistrationsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth', obtain_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/', CustomRegistrationsView.as_view(), name='register'),
]
