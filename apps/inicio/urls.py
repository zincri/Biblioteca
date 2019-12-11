#from django.contrib import admin
from django.urls import path, include
from .views import  vista_inicio
from django.contrib.auth.views import LoginView,LogoutView
#from apps.inicio.api.routers import router
urlpatterns = [
    path('',vista_inicio,name="inicio"),
    #path('api/',include(router.urls)),    
]

