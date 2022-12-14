# Generated by Django 4.0.3 on 2022-08-03 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_school_edu_levels_alter_userfavorite_schools'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='year_founded',
            field=models.CharField(default=2000, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='cel',
            field=models.CharField(default='00-00-00-00', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='moto',
            field=models.CharField(default='slogan', max_length=255),
        ),
        migrations.AlterField(
            model_name='school',
            name='tel',
            field=models.CharField(default='00-00-00-00', max_length=255),
        ),
    ]
