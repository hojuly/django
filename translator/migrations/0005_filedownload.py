# Generated by Django 3.1.3 on 2021-01-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0004_remove_fileupload_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dw_file', models.FileField(blank=True, null=True, upload_to='', verbose_name='file')),
            ],
        ),
    ]
