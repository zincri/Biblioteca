from django.shortcuts import render
from apps.inicio.models import Prestador
# Create your views here.
def vista_inicio(request):
    users = Prestador.objects.all()
    return render(request,"inicio/inicio.html",{'users':users})