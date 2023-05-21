from django.shortcuts import render, redirect
from .forms.RecomendacionesForm import RecomendacionesForm
from .models import Recomendaciones, Usuarios, Dietas

def crear_recomendaciones(request):
    usuarios = Usuarios.objects.all()
    dietas = Dietas.objects.all()
    if request.method == 'POST':
        recomendacion = RecomendacionesForm(request.POST)
        if recomendacion.is_valid():
            recomendacion.save()
            return redirect('lista_recomendaciones')
    return render(request, 'crear_recomendaciones.html', {'dietas':dietas},{'usuarios': usuarios})

def lista_recomendaciones(request):
    recomendaciones = Recomendaciones.objects.all()
    return render(request, 'lista_recomendaciones.html', {'recomendaciones': recomendaciones})

def detalle_recomendaciones(request, id):
    recomendacion = Recomendaciones.objects.get(id=id)
    return render(request, 'detalle_recomendaciones.html', {'recomendacion': recomendacion})

#Metodo para actualizar un dieta
def actualizar_recomendaciones(request, id):
    recomendacion = RecomendacionesForm.objects.get(id=id)
    usuarios = usuarios.objects.all()
    dietas = dietas.objects.all()
    if request.method == 'POST':
        form = RecomendacionesForm(request.POST, instance=recomendacion)
        if form.is_valid():
            form.save()
            return redirect('lista_recomendaciones')
    return render(request, 'actualizar_recomendaciones.html', {'recomendacion': recomendacion}, {'dietas':dietas},{'usuarios': usuarios})

#Metodo para eliminar un dieta
def eliminar_recomendaciones(request, id):
    recomendacion = Recomendaciones.objects.get(id=id)
    if request.method == 'POST':
        recomendacion.delete()
        return redirect('lista_recomendaciones')
    return render(request, 'eliminar_recomendaciones.html', {'recomendacion': recomendacion})