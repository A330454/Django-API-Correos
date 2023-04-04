from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FormularioContacto
from django.http import HttpResponse

def index(request):

    return render(request,"correo/home.html")

def correo(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            # email=request.POST.get("email")
            email="vicort6@gmail.com"
            contenido=request.POST.get("contenido")

            email = send_mail(nombre, email, contenido, "correo")

            try:
                email.send()

                return redirect("/correo/?valido")
            except:
                
                return redirect("/correo/?novalido")

    return render(request, "correo/correo.html", {'miFormulario':formulario_contacto})
# Create your views here.

def send_mail(nombre:str, email, contenido, receptor:str):
    return EmailMessage("Mensaje de app Django",
    "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), 
    '',
    [receptor], 
    reply_to=[email])
