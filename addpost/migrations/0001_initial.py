# Generated by Django 3.0.2 on 2020-01-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='room/pdfs')),
                ('location', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]