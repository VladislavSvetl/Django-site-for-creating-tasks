# Generated by Django 4.1.3 on 2022-12-03 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='task',
            name='number',
        ),
    ]