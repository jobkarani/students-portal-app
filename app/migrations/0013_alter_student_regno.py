# Generated by Django 3.2.8 on 2022-04-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220423_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='regno',
            field=models.CharField(help_text='Eg- sct-121,sct-220,sct-560etc', max_length=100, unique=True),
        ),
    ]