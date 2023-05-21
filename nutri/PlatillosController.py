from django.shortcuts import render, redirect
from .forms.PlatillosForm import PlatillosForm
from .models import Platillos

#Metodo para crear un platillo
def crear_platillo(request):
    if request.method == 'POST':
        platillo = PlatillosForm(request.POST)
        if platillo.is_valid():
            platillo.save()
            return redirect('lista_platillos')
    return render(request, 'crear_platillo.html')

#Metodo enlistar a los platillos
def lista_platillos(request):
    platillos = Platillos.objects.all()
    return render(request, 'lista_platillos.html', {'platillos': platillos})

#Metodo para ver los detalles de un platillo
def detalle_platillo(request, id):
    platillo = Platillos.objects.get(id=id)
    return render(request, 'detalle_platillo.html', {'platillo': platillo})

#Metodo para actualizar un platillo
def actualizar_platillo(request, id):
    platillo = Platillos.objects.get(id=id)
    if request.method == 'POST':
        form = PlatillosForm(request.POST, instance=platillo)
        if form.is_valid():
            form.save()
            return redirect('lista_platillos')
    return render(request, 'actualizar_platillo.html', {'platillo': platillo})

#Metodo para eliminar un platillo
def eliminar_platillo(request, id):
    platillo = Platillos.objects.get(id=id)
    if request.method == 'POST':
        platillo.delete()
        return redirect('lista_platillos')
    return render(request, 'eliminar_platillo.html', {'platillo': platillo})