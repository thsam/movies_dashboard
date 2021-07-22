# Generated by Django 3.2.5 on 2021-07-19 01:26
from proyecto.models import Movies

from django.db import migrations

def datos(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    f = open("./proyecto/finalfinal.txt", "r")

    for linea in f:
        #print(linea.split(',')[0])
        l=linea.split('\t\t')
        agregar=Movies.objects.create(
            movie=str(l[0]),
            user=str(l[1]),
            profilename=str(l[2]),
            helpfulness=str(l[3]),
            score=l[4],
            date=l[5],
            summary=l[6]
        )
        agregar.save()

    f.close()
class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0004_auto_20210718_2008'),
    ]

    operations = [
        migrations.RunPython(datos),
    ]