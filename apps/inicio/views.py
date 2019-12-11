from django.shortcuts import render
from apps.inicio.models import Lender
# Create your views here.
def vista_inicio(request):
    users = Lender.objects.all()
    return render(request,"inicio/inicio.html",{'users':users})