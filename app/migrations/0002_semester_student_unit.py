# Generated by Django 3.2.9 on 2022-04-21 07:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(help_text='Eg-one, two,three etc', max_length=100)),
                ('semester_name_in_numeric', models.IntegerField(help_text='Eg- 1,2,4,5 etc')),
                ('section', models.CharField(help_text='Eg- A,B,C etc', max_length=10)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=100)),
                ('unit_code', models.IntegerField()),
                ('unit_creation_date', models.DateTimeField(auto_now_add=True)),
                ('unit_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=8)),
                ('dob', models.DateField(default=datetime.date(2022, 4, 21))),
                ('regno', models.DateField(auto_now_add=True)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.semester')),
            ],
        ),
    ]
