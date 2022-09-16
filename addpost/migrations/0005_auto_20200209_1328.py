# Generated by Django 3.0.2 on 2020-02-09 07:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('addpost', '0004_auto_20200209_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='location',
        ),
        migrations.AddField(
            model_name='room',
            name='location',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]