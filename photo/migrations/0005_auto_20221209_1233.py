# Generated by Django 3.2 on 2022-12-09 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20221209_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_load',
            field=models.DateField(auto_created=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='names_of_people',
            field=models.ManyToManyField(blank=True, to='photo.UserName', verbose_name='Люди на фото'),
        ),
    ]
