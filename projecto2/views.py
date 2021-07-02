from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *
# Create your views here.
def computador_view(request):
    return render(request, "projecto2/computadores.html")

def tablet_view(request):
    return render(request, "projecto2/tablet.html")

def home_view(request):
    return render(request, "projecto2/home.html")

def telefone_view(request):
    return render(request, "projecto2/telemoveis.html")

def encomenda_view(request):
    formulario = EncomendarForms
    context = {"encomenda": formulario}
    return render(request, "projecto2/encomenda.html", context)

def informa_view (request):
    return render(request, "projecto2/informacao.html")

def sobre_view(request):
    formulario = SobreForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return render(request, "projecto2/home.html")
    context = {"formulario": formulario}
    return render(request, "projecto2/Sobre.html", context)

def contacto_view (request):
    formulario = ContactForms(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return render(request, "projecto2/home.html")
    context = {"formulario": formulario}
    return render(request, "projecto2/contacto.html", context)

