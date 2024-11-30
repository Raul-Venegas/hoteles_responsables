# Generated by Django 4.2.14 on 2024-11-29 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('open', 'Pregunta abierta'), ('multiple_choice', 'Opción múltiple')], default='multiple_choice', max_length=20),
        ),
        migrations.AddField(
            model_name='resultado',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
