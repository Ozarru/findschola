# Generated by Django 4.0.3 on 2022-08-03 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EduLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('tel', models.CharField(default='97998621', max_length=255)),
                ('cel', models.CharField(default='97998621', max_length=255)),
                ('moto', models.CharField(default='school moto', max_length=255)),
                ('history', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('teacher_count', models.IntegerField(default='0')),
                ('student_count', models.IntegerField(default='0')),
                ('classe_count', models.IntegerField(default='0')),
                ('lab_count', models.IntegerField(default='0')),
                ('success_rate', models.IntegerField(default='0')),
                ('is_featured', models.BooleanField(default='false')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='schools/thumbnails')),
                ('crest', models.ImageField(blank=True, null=True, upload_to='schools/crests')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('edu_levels', models.ManyToManyField(null=True, to='base.edulevel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schools', models.ManyToManyField(null=True, to='base.school')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='schools/images', verbose_name='Image')),
                ('listing', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.school')),
            ],
        ),
    ]
