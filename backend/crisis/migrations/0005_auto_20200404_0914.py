# Generated by Django 3.0.3 on 2020-04-04 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0004_auto_20200404_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='profile_pics')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
