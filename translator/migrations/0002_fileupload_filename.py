# Generated by Django 3.1.3 on 2021-01-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='filename',
            field=models.CharField(max_length=64, null=True, verbose_name='filename'),
        ),
    ]