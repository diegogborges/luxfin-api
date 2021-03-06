# Generated by Django 3.1.3 on 2021-01-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('due', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='due_definition',
            name='day_pay',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='due_definition',
            name='time_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='due_definition',
            name='time_initial',
            field=models.DateField(blank=True, null=True),
        ),
    ]