# Generated by Django 2.0.dev20170514183117 on 2017-06-21 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Destacada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_destacada', models.DateField()),
            ],
            options={
                'ordering': ['fecha_destacada'],
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(blank=True, height_field='alto_imagen', null=True, upload_to='', width_field='ancho_imagen')),
                ('alto_imagen', models.IntegerField(default=0)),
                ('ancho_imagen', models.IntegerField(default=0)),
                ('fecha', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='destacada',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Noticia'),
        ),
    ]