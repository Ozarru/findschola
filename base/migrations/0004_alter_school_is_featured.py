# Generated by Django 4.0.3 on 2022-08-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_school_year_founded_alter_school_cel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
