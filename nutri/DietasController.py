from django.shortcuts import render, redirect
from .forms.DietasForm import DietasForm
from .models import Dietas

#Metodo para crear un dieta
def crear_dieta(request):
    if request.method == 'POST':
        dieta = DietasForm(request.POST)
        if dieta.is_valid():
            dieta.save()
            return redirect('lista_dietas')
    return render(request, 'crear_dieta.html')

#Metodo enlistar a los dietas
def lista_dietas(request):
    dietas = Dietas.objects.all()
    return render(request, 'lista_dietas.html', {'dietas': dietas})

#Metodo para ver los detalles de un dieta
def detalle_dieta(request, id):
    dieta = Dietas.objects.get(id=id)
    return render(request, 'detalle_dieta.html', {'dieta': dieta})

#Metodo para actualizar un dieta
def actualizar_dieta(request, id):
    dieta = Dietas.objects.get(id=id)
    if request.method == 'POST':
        form = DietasForm(request.POST, instance=dieta)
        if form.is_valid():
            form.save()
            return redirect('lista_dietas')
    return render(request, 'actualizar_dieta.html', {'dieta': dieta})

#Metodo para eliminar un dieta
def eliminar_dieta(request, id):
    dieta = Dietas.objects.get(id=id)
    if request.method == 'POST':
        dieta.delete()
        return redirect('lista_dietas')
    return render(request, 'eliminar_dieta.html', {'dieta': dieta})