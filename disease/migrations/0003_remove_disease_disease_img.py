# Generated by Django 4.1.7 on 2023-04-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0002_alter_disease_disease_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='disease_Img',
        ),
    ]
