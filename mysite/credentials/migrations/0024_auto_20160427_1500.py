# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-27 09:30
from __future__ import unicode_literals

import credentials.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0023_auto_20160426_1945'),
    ]

    operations = [
        migrations.CreateModel(
            name='logom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('imagename', models.CharField(max_length=100, null=True)),
                ('upload', models.ImageField(null=True, upload_to=credentials.models.get_upload_logoname)),
            ],
        ),
        migrations.CreateModel(
            name='planguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('languages_known', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='benefits',
            new_name='benefitsm',
        ),
        migrations.RenameModel(
            old_name='Work',
            new_name='headofficem',
        ),
        migrations.RenameModel(
            old_name='jobprofile',
            new_name='jobprofilem',
        ),
        migrations.RenameModel(
            old_name='overview',
            new_name='overviewm',
        ),
        migrations.RenameModel(
            old_name='headoffice',
            new_name='Sales_officem',
        ),
        migrations.RenameModel(
            old_name='statistics',
            new_name='statisticsm',
        ),
        migrations.RenameModel(
            old_name='Sales_office',
            new_name='Workm',
        ),
        migrations.DeleteModel(
            name='language',
        ),
        migrations.DeleteModel(
            name='logo',
        ),
        migrations.AlterField(
            model_name='contact',
            name='upload_cv',
            field=models.FileField(null=True, upload_to='cvfiles'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='imagename',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sec',
            name='school',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='srsec',
            name='school',
            field=models.CharField(max_length=40),
        ),
    ]
