# Generated by Django 4.1.1 on 2022-10-17 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_alter_superhero_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superhero',
            name='author',
        ),
    ]
