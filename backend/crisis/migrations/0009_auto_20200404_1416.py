# Generated by Django 3.0.3 on 2020-04-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0008_auto_20200404_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='test'),
        ),
    ]
