from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormForm
from django.urls import reverse

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes_publicos': flanes_publicos,
    }
    return render(request, "index.html", context)

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {
        'flanes_privados': flanes_privados,
    }
    return render(request, "welcome.html", context)

def about(request):
    return render(request, "about.html", {})

def base(request):
    return render(request, "base.html", {})

def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/exito")
    else:
        form = ContactFormForm()
    
    return render(request, "contacto.html", {"form": form})

def exito(request):
    return render(request, "exito.html", {})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', reverse('welcome'))
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def detalles(request):
    flanes = Flan.objects.filter()
    context = {
        'flanes': flanes,
    }
    return render(request, "detalles.html", context)