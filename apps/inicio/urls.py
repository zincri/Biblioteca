#from django.contrib import admin
from django.urls import path, include
from .views import  vista_inicio
from django.contrib.auth.views import LoginView,LogoutView
from apps.inicio.api.routers import router
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('',login_required(vista_inicio),name="inicio"),
    path('login/',LoginView.as_view(template_name="auth/login.html"),name="login"),
    path('cerrar/',LogoutView.as_view(template_name="auth/login.html"),name="logout"),
    path('api/',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

