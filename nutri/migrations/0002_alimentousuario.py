# Generated by Django 4.2.1 on 2023-05-21 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlimentoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutri.platillos')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutri.usuarios')),
            ],
        ),
    ]