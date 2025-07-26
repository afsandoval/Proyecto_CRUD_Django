from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido a la Librería</h1>")

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def libros(request):
    return render(request,'libros/index.html')