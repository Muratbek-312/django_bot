# Generated by Django 3.1.4 on 2020-12-25 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botson', '0002_stadup_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadup',
            name='first_answer',
            field=models.TextField(verbose_name='Сделано'),
        ),
        migrations.AlterField(
            model_name='stadup',
            name='second_answer',
            field=models.TextField(verbose_name='Планы'),
        ),
        migrations.AlterField(
            model_name='stadup',
            name='third_answer',
            field=models.TextField(verbose_name='Сложности которые возникли'),
        ),
    ]
