# Generated by Django 3.0.3 on 2020-04-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0002_auto_20200404_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='count',
            field=models.CharField(blank=True, default=0, max_length=50),
        ),
    ]
