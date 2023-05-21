from django.shortcuts import render, redirect
from .forms.AlimentoUsuarioForm import AlimentoUsuarioForm
from .models import AlimentoUsuario, Usuarios, Platillos

def crear_alimentousuario(request):
    usuarios = Usuarios.objects.all()
    platillos = Platillos.objects.all()
    if request.method == 'POST':
        alimento = AlimentoUsuarioForm(request.POST)
        if alimento.is_valid():
            alimento.save()
            return redirect('lista_alimentousuario')
    return render(request, 'crear_alimentousuario.html', {'platillos':platillos},{'usuarios': usuarios})

def lista_alimentousuario(request):
    alimentousuario = AlimentoUsuario.objects.all()
    return render(request, 'lista_alimentousuario.html', {'alimentousuario': alimentousuario})

def detalle_alimentousuario(request, id):
    alimento = AlimentoUsuario.objects.get(id=id)
    return render(request, 'detalle_alimentousuario.html', {'alimento': alimento})

def actualizar_alimentousuario(request, id):
    alimento = AlimentoUsuarioForm.objects.get(id=id)
    usuarios = Usuarios.objects.all()
    platillos = Platillos.objects.all()
    if request.method == 'POST':
        form = AlimentoUsuarioForm(request.POST, instance=alimento)
        if form.is_valid():
            form.save()
            return redirect('lista_alimentousuario')
    return render(request, 'actualizar_alimentousuario.html', {'alimento': alimento}, {'platillos':platillos},{'usuarios': usuarios})

def eliminar_alimentousuario(request, id):
    alimento = AlimentoUsuario.objects.get(id=id)
    if request.method == 'POST':
        alimento.delete()
        return redirect('lista_alimentousuario')
    return render(request, 'eliminar_alimentousuario.html', {'alimento': alimento})