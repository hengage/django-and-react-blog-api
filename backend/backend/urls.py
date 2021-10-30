from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/', include('users.urls', namespace='users')),
    path(
        'api/token/', 
        jwt_views.TokenObtainPairView.as_view(), 
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', 
        jwt_views.TokenRefreshView.as_view(), 
        name='token_refresh'
    ),

]
