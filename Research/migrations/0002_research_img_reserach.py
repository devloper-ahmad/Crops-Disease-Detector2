# Generated by Django 4.1.7 on 2023-04-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Research', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='img_Reserach',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='medicine2/'),
        ),
    ]
