# Generated by Django 4.2 on 2023-06-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]