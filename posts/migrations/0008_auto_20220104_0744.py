# Generated by Django 3.2.5 on 2022-01-04 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_rename_sneezingwithoutcoveringyour_mouth_post_sneezingwithoutcoveringyourmouth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='commercial',
            new_name='fields',
        ),
        migrations.RemoveField(
            model_name='post',
            name='IT',
        ),
        migrations.RemoveField(
            model_name='post',
            name='arts',
        ),
        migrations.RemoveField(
            model_name='post',
            name='science',
        ),
    ]