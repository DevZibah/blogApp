# Generated by Django 3.2.5 on 2022-01-02 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211229_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='christian',
        ),
        migrations.RemoveField(
            model_name='post',
            name='north_central',
        ),
        migrations.RemoveField(
            model_name='post',
            name='north_east',
        ),
        migrations.RemoveField(
            model_name='post',
            name='north_west',
        ),
        migrations.RemoveField(
            model_name='post',
            name='south_east',
        ),
        migrations.RemoveField(
            model_name='post',
            name='south_south',
        ),
        migrations.RemoveField(
            model_name='post',
            name='south_west',
        ),
        migrations.AddField(
            model_name='post',
            name='AB',
            field=models.BooleanField(default=False, verbose_name='AB'),
        ),
        migrations.AddField(
            model_name='post',
            name='AD',
            field=models.BooleanField(default=False, verbose_name='AD'),
        ),
        migrations.AddField(
            model_name='post',
            name='AI',
            field=models.BooleanField(default=False, verbose_name='AI'),
        ),
        migrations.AddField(
            model_name='post',
            name='AN',
            field=models.BooleanField(default=False, verbose_name='AN'),
        ),
        migrations.AddField(
            model_name='post',
            name='BA',
            field=models.BooleanField(default=False, verbose_name='BA'),
        ),
        migrations.AddField(
            model_name='post',
            name='BN',
            field=models.BooleanField(default=False, verbose_name='BN'),
        ),
        migrations.AddField(
            model_name='post',
            name='BR',
            field=models.BooleanField(default=False, verbose_name='BR'),
        ),
        migrations.AddField(
            model_name='post',
            name='BY',
            field=models.BooleanField(default=False, verbose_name='BY'),
        ),
        migrations.AddField(
            model_name='post',
            name='CR',
            field=models.BooleanField(default=False, verbose_name='CR'),
        ),
        migrations.AddField(
            model_name='post',
            name='DL',
            field=models.BooleanField(default=False, verbose_name='DL'),
        ),
        migrations.AddField(
            model_name='post',
            name='EB',
            field=models.BooleanField(default=False, verbose_name='EB'),
        ),
        migrations.AddField(
            model_name='post',
            name='ED',
            field=models.BooleanField(default=False, verbose_name='ED'),
        ),
        migrations.AddField(
            model_name='post',
            name='EK',
            field=models.BooleanField(default=False, verbose_name='EK'),
        ),
        migrations.AddField(
            model_name='post',
            name='EN',
            field=models.BooleanField(default=False, verbose_name='EN'),
        ),
        migrations.AddField(
            model_name='post',
            name='FC',
            field=models.BooleanField(default=False, verbose_name='FC'),
        ),
        migrations.AddField(
            model_name='post',
            name='GM',
            field=models.BooleanField(default=False, verbose_name='GM'),
        ),
        migrations.AddField(
            model_name='post',
            name='IM',
            field=models.BooleanField(default=False, verbose_name='IM'),
        ),
        migrations.AddField(
            model_name='post',
            name='JI',
            field=models.BooleanField(default=False, verbose_name='JI'),
        ),
        migrations.AddField(
            model_name='post',
            name='KA',
            field=models.BooleanField(default=False, verbose_name='KA'),
        ),
        migrations.AddField(
            model_name='post',
            name='KB',
            field=models.BooleanField(default=False, verbose_name='KB'),
        ),
        migrations.AddField(
            model_name='post',
            name='KG',
            field=models.BooleanField(default=False, verbose_name='KG'),
        ),
        migrations.AddField(
            model_name='post',
            name='KN',
            field=models.BooleanField(default=False, verbose_name='KN'),
        ),
        migrations.AddField(
            model_name='post',
            name='KS',
            field=models.BooleanField(default=False, verbose_name='KS'),
        ),
        migrations.AddField(
            model_name='post',
            name='KW',
            field=models.BooleanField(default=False, verbose_name='KW'),
        ),
        migrations.AddField(
            model_name='post',
            name='LA',
            field=models.BooleanField(default=False, verbose_name='LA'),
        ),
        migrations.AddField(
            model_name='post',
            name='NA',
            field=models.BooleanField(default=False, verbose_name='NA'),
        ),
        migrations.AddField(
            model_name='post',
            name='NI',
            field=models.BooleanField(default=False, verbose_name='NI'),
        ),
        migrations.AddField(
            model_name='post',
            name='OG',
            field=models.BooleanField(default=False, verbose_name='OG'),
        ),
        migrations.AddField(
            model_name='post',
            name='ON',
            field=models.BooleanField(default=False, verbose_name='ON'),
        ),
        migrations.AddField(
            model_name='post',
            name='OS',
            field=models.BooleanField(default=False, verbose_name='OS'),
        ),
        migrations.AddField(
            model_name='post',
            name='OY',
            field=models.BooleanField(default=False, verbose_name='OY'),
        ),
        migrations.AddField(
            model_name='post',
            name='PT',
            field=models.BooleanField(default=False, verbose_name='PT'),
        ),
        migrations.AddField(
            model_name='post',
            name='RV',
            field=models.BooleanField(default=False, verbose_name='RV'),
        ),
        migrations.AddField(
            model_name='post',
            name='ST',
            field=models.BooleanField(default=False, verbose_name='ST'),
        ),
        migrations.AddField(
            model_name='post',
            name='TB',
            field=models.BooleanField(default=False, verbose_name='TB'),
        ),
        migrations.AddField(
            model_name='post',
            name='YB',
            field=models.BooleanField(default=False, verbose_name='YB'),
        ),
        migrations.AddField(
            model_name='post',
            name='ZF',
            field=models.BooleanField(default=False, verbose_name='ZF'),
        ),
        migrations.AddField(
            model_name='post',
            name='christianity',
            field=models.BooleanField(default=False, verbose_name='christianity'),
        ),
    ]
