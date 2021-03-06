# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-01 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0009_internships'),
    ]

    operations = [
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('languages_known', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('links', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='postgrad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('yearofpassing', models.IntegerField()),
                ('Last_spi', models.FloatField(max_length=10)),
                ('Cpi', models.FloatField(max_length=10)),
                ('Branch_of_study', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=40)),
                ('position', models.CharField(max_length=40)),
                ('duration', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('projects_related_url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('yearofpassing', models.IntegerField()),
                ('percentage_or_cpi', models.FloatField(max_length=10)),
                ('school', models.CharField(max_length=10)),
                ('Board', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='srsec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('yearofpassing', models.IntegerField()),
                ('percentage_obtained', models.FloatField(max_length=10)),
                ('school', models.CharField(max_length=10)),
                ('Board', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='undergrad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('yearofpassing', models.IntegerField()),
                ('Last_spi', models.FloatField(max_length=10)),
                ('Cpi', models.FloatField(max_length=10)),
                ('Branch_of_study', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='company',
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='internships',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='internships',
            name='email',
            field=models.EmailField(max_length=20),
        ),
    ]
