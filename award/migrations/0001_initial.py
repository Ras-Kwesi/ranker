# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 09:06
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentvote', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Creativity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creativityvote', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designvote', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=100)),
                ('profilepic', models.ImageField(blank=True, upload_to='picture/')),
                ('contact', models.CharField(blank=True, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=40)),
                ('overview', models.CharField(max_length=100)),
                ('image1', models.ImageField(blank=True, upload_to='picture/')),
                ('image2', models.ImageField(blank=True, upload_to='picture/')),
                ('image3', models.ImageField(blank=True, upload_to='picture/')),
                ('likes', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usabilityvote', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('usability_voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userbility_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usabilityvote', to='award.Project')),
            ],
        ),
        migrations.AddField(
            model_name='design',
            name='design_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designvote', to='award.Project'),
        ),
        migrations.AddField(
            model_name='design',
            name='design_voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='creativity',
            name='creativity_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creativityvote', to='award.Project'),
        ),
        migrations.AddField(
            model_name='creativity',
            name='creativity_voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='content_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contentvote', to='award.Project'),
        ),
        migrations.AddField(
            model_name='content',
            name='content_voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
