# Generated by Django 3.1.1 on 2020-09-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20200929_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
