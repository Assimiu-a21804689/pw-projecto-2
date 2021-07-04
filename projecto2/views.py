from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

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


def contactos_view(request):
    if not request.user.is_authenticated:
        return render(request, "projecto2/login.html")
    context = {"contactos": Contacto.objects.all()}
    return render(request, "projecto2/contactos.html", context)

def login_view(request):
    if request.POST:
        username = request.POST['email']
        password = request.POST['senha']
        usuario = authenticate(username= username, password=password)


        contact = Contacto.objects.all()
        if usuario is not None:
            login(request, usuario)
            return render(request, "projecto2/contactos.html", {"contactos": contact})
        return render(request, "projecto2/login.html", {"mensag": "Senha ou email inválido"})


def apagar_view (request, pk):
    pessoa = Contacto.objects.get(pk=pk)
    if pessoa !=  None:
        pessoa.delete()
    return render(request, "projecto2/home.html")

def editar_view (request, pk):
    idPessoa = Contacto.objects.get(pk=pk)
    pessoa = ContactForms(request.POST or None, instance=idPessoa)

    if pessoa.is_valid():
        pessoa.save()
        return render(request, "projecto2/home.html")
    return render(request, "projecto2/editar.html", {"idPessoa": idPessoa, "pessoa": pessoa})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, "projecto2/home.html")

def quiz_view(request):
    return render(request, "projecto2/quizz.html")








