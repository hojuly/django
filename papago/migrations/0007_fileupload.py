# Generated by Django 3.1.3 on 2021-01-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papago', '0006_auto_20210126_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('up_file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
