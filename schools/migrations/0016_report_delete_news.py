# Generated by Django 4.1 on 2022-08-05 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0015_alter_news_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='schools/reports')),
                ('title', models.CharField(default='News Title', max_length=255)),
                ('subtitle', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(blank=True, default='News')),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
