from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm #ContactFormForm

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
        form = ContactFormModelForm(request.POST) #ContactFormForm(request.POST)
        if form.is_valid():
            #contact_form = ContactForm.objects.create(**form.cleaned_data)
            form.save()
            return HttpResponseRedirect("/exito")
    else:
        form = ContactFormModelForm() #ContactFormForm()
    
    return render(request, "contacto.html", {"form": form})

def exito(request):
    return render(request, "exito.html", {})