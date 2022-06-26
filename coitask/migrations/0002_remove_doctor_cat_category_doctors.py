# Generated by Django 4.0.5 on 2022-06-25 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coitask', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='cat',
        ),
        migrations.AddField(
            model_name='category',
            name='doctors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coitask.doctor'),
        ),
    ]