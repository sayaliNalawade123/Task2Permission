
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh



urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/',include('post_app.urls')),
    path('access/',token_obtain_pair),
    path('refresh/',token_refresh),
    path('register/',include('auth_app.urls')),
    
   
]
