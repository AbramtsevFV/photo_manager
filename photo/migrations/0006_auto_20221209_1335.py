# Generated by Django 3.2 on 2022-12-09 13:35

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_auto_20221209_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_load',
            field=models.DateField(auto_created=True, default=django.utils.datetime_safe.date.today, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='names_of_people',
            field=models.ManyToManyField(blank=True, null=True, to='photo.UserName', verbose_name='Люди на фото'),
        ),
    ]
