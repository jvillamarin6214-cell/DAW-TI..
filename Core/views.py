from django.shortcuts import render
from portafolio.models import Proyecto
def home(request):
    return render(request, template_name="Core/home.html")

def about(request):
    return render(request, template_name="Core/about.html")

def portafolio(request):
    # Aquí pedimos todos los proyectos que subiste al admin
    proyectos = Proyecto.objects.all()
    return render(request, "Core/Portafolio.html", {'proyectos': proyectos})

def contacto(request):
    return render(request, template_name="Core/Contacto.html")