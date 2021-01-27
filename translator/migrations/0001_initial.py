# Generated by Django 3.1.3 on 2021-01-26 08:03

from django.db import migrations, models
import translator.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_file', models.FileField(blank=True, null=True, upload_to=translator.models.get_file_path, verbose_name='file')),
            ],
        ),
    ]