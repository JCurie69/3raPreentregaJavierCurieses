from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,"appent03/inivio.html")

def cursos(request):
    return render(request)

def estudiantes(request):
    return render(request)

def profesores(request):
    return render(request)

def entregables(request):
    return render(request)
