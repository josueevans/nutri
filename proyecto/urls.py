"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from nutri import views, UsuariosController, RecomendacionesController, PlatillosController, DietasController, DietasPlatillosController, AlimentoUsuarioController

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('ruta/', views.index, name='nombre_vista'),
    path('', views.index, name='nombre_vista'),


    path('crear-usuario/', UsuariosController.crear_usuario, name='crear_usuario'),
    path('lista-usuarios/', UsuariosController.lista_usuarios, name='lista_usuarios'),
    path('detalle-usuario/<int:id>/', UsuariosController.detalle_usuario, name='detalle_usuario'),
    path('actualizar-usuario/<int:id>/', UsuariosController.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar-usuario/<int:id>/', UsuariosController.eliminar_usuario, name='eliminar_usuario'),

    path('crear-platillo/', PlatillosController.crear_platillo, name='crear_platillo'),
    path('lista-platillos/', PlatillosController.lista_platillos, name='lista_platillos'),
    path('detalle-platillo/<int:id>/', PlatillosController.detalle_platillo, name='detalle_platillo'),
    path('actualizar-platillo/<int:id>/', PlatillosController.actualizar_platillo, name='actualizar_platillo'),
    path('eliminar-platillo/<int:id>/', PlatillosController.eliminar_platillo, name='eliminar_platillo'),

    path('crear-dieta/', DietasController.crear_dieta, name='crear_dieta'),
    path('lista-dietas/', DietasController.lista_dietas, name='lista_dietas'),
    path('detalle-dieta/<int:id>/', DietasController.detalle_dieta, name='detalle_dieta'),
    path('actualizar-dieta/<int:id>/', DietasController.actualizar_dieta, name='actualizar_dieta'),
    path('eliminar-dieta/<int:id>/', DietasController.eliminar_dieta, name='eliminar_dieta'),

    path('crear-dietaplatillo/', DietasPlatillosController.crear_dietaplatillo, name='crear_dietaplatillo'),
    path('lista-dietaplatillos/', DietasPlatillosController.lista_dietasplatillos, name='lista_dietasplatillos'),
    path('detalle-dietaplatillo/<int:id>/', DietasPlatillosController.detalle_dietaplatillo, name='detalle_dietaplatillo'),
    path('actualizar-dietaplatillo/<int:id>/', DietasPlatillosController.actualizar_dietaplatillo, name='actualizar_dietaplatillo'),
    path('eliminar-dietaplatillo/<int:id>/', DietasPlatillosController.eliminar_dietaplatillo, name='eliminar_dietaplatillo'),

    path('crear-recomendacion/', RecomendacionesController.crear_recomendaciones, name='crear_recomendacion'),
    path('lista-recomendaciones/', RecomendacionesController.lista_recomendaciones, name='lista_recomendaciones'),
    path('detalle-recomendacion/<int:id>/', RecomendacionesController.detalle_recomendaciones, name='detalle_recomendacion'),
    path('actualizar-recomendacion/<int:id>/', RecomendacionesController.actualizar_recomendaciones, name='actualizar_recomendacion'),
    path('eliminar-recomendacion/<int:id>/', RecomendacionesController.eliminar_recomendaciones, name='eliminar_recomendacion'),

    path('crear-alimento/', AlimentoUsuarioController.crear_alimentousuario, name='crear_alimento'),
    path('lista-alimentos/', AlimentoUsuarioController.lista_alimentousuario, name='lista_alimentos'),
    path('detalle-alimento/<int:id>/', AlimentoUsuarioController.detalle_alimentousuario, name='detalle_alimento'),
    path('actualizar-alimento/<int:id>/', AlimentoUsuarioController.actualizar_alimentousuario, name='actualizar_alimento'),
    path('eliminar-alimento/<int:id>/', AlimentoUsuarioController.eliminar_alimentousuario, name='eliminar_alimento'),
]

