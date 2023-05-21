from django.shortcuts import render, redirect
from .forms.DietasPlatillosForm import DietasPlatillosForm
from .models import DietasPlatillos, Dietas, Platillos

#Metodo para crear un dieta
def crear_dietaplatillo(request):
    dietas = Dietas.objects.all()
    platillos = Platillos.objects.all()
    if request.method == 'POST':
        dieta = DietasPlatillosForm(request.POST)
        if dieta.is_valid():
            dieta.save()
            return redirect('lista_dietasplatillos')
    return render(request, 'crear_dietaplatillo.html', {'platillos':platillos},{'dietas': dietas})

#Metodo enlistar a los dietas
def lista_dietasplatillos(request):
    dietas = DietasPlatillos.objects.all()
    return render(request, 'lista_dietasplatillos.html', {'dietas': dietas})

#Metodo para ver los detalles de un dieta
def detalle_dietaplatillo(request, id):
    dieta = DietasPlatillos.objects.get(id=id)
    return render(request, 'detalle_dietaplatillo.html', {'dieta': dieta})

#Metodo para actualizar un dieta
def actualizar_dietaplatillo(request, id):
    dieta = DietasPlatillosForm.objects.get(id=id)
    dietas = Dietas.objects.all()
    platillos = Platillos.objects.all()
    if request.method == 'POST':
        dieta = DietasPlatillosForm(request.POST, instance=dieta)
        if dieta.is_valid():
            dieta.save()
            return redirect('lista_dietasplatillos')
    return render(request, 'actualizar_dietaplatillo.html', {'dieta': dieta}, {'platillos':platillos},{'dietas': dietas})

#Metodo para eliminar un dieta
def eliminar_dietaplatillo(request, id):
    dieta = DietasPlatillos.objects.get(id=id)
    if request.method == 'POST':
        dieta.delete()
        return redirect('lista_dietasplatillos')
    return render(request, 'eliminar_dietaplatillo.html', {'dieta': dieta})