from django.db import models

class Platillos(models.Model):
    nombre = models.CharField(max_length=255)
    caloriasPorPorcion = models.FloatField()
    proteinasPorPorcion = models.FloatField()
    carbohidratosPorPorcion = models.FloatField()
    grasasPorPorcion = models.FloatField()

class Dietas(models.Model):
    tipo = models.CharField(max_length=255)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

class DietasPlatillos(models.Model):
    comida = models.CharField(max_length=255)
    id_dieta = models.ForeignKey(Dietas, on_delete=models.CASCADE)
    id_platillo = models.ForeignKey(Platillos, on_delete=models.CASCADE)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    genero = models.CharField(max_length=255)
    nivelActividad = models.CharField(max_length=255)

class Recomendaciones(models.Model):
    recomendacion = models.TextField()
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_dieta = models.ForeignKey(Dietas, on_delete=models.CASCADE)


class AlimentoUsuario(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_platillo = models.ForeignKey(Platillos, on_delete=models.CASCADE)