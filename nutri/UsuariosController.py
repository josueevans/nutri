from django.shortcuts import render, redirect
from .forms.UsuariosForm import UsuariosForm
from .models import Usuarios

#Metodo para crear un usuario
def crear_usuario(request):
    if request.method == 'POST':
        usuario = UsuariosForm(request.POST)
        if usuario.is_valid():
            usuario.save()
            return redirect('lista_usuarios')
    return render(request, 'crear_usuario.html')

#Metodo enlistar a los usuarios
def lista_usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

#Metodo para ver los detalles de un usuario
def detalle_usuario(request, id):
    usuario = Usuarios.objects.get(id=id)
    return render(request, 'detalle_usuario.html', {'usuario': usuario})

#Metodo para actualizar un usuario
def actualizar_usuario(request, id):
    usuario = Usuarios.objects.get(id=id)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    return render(request, 'actualizar_usuario.html', {'usuario': usuario})

#Metodo para eliminar un usuario
def eliminar_usuario(request, id):
    usuario = Usuarios.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'eliminar_usuario.html', {'usuario': usuario})