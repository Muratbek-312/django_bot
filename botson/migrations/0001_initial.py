# Generated by Django 3.1.4 on 2020-12-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stadup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('first_answer', models.TextField()),
                ('second_answer', models.TextField()),
                ('third_answer', models.TextField()),
            ],
        ),
    ]