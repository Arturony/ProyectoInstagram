# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 01:04
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MiUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.CharField(max_length=100, null=True)),
                ('estado', models.CharField(max_length=300, null=True)),
                ('usuario_django', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.MiUsuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_photo', models.CharField(max_length=100)),
            ],
        ),
    ]
