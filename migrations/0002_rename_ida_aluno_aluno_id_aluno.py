# Generated by Django 5.1.1 on 2024-10-17 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refeitorioApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aluno',
            old_name='ida_Aluno',
            new_name='id_aluno',
        ),
    ]
