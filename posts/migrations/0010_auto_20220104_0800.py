# Generated by Django 3.2.5 on 2022-01-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20220104_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='IT',
            field=models.BooleanField(default=False, verbose_name='IT'),
        ),
        migrations.AlterField(
            model_name='post',
            name='arts',
            field=models.BooleanField(default=False, verbose_name='arts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='commercial',
            field=models.BooleanField(default=False, verbose_name='commercial'),
        ),
        migrations.AlterField(
            model_name='post',
            name='science',
            field=models.BooleanField(default=False, verbose_name='science'),
        ),
    ]
