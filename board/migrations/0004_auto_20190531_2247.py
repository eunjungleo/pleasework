# Generated by Django 2.2.1 on 2019-05-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20190516_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, upload_to='storedimages/'),
        ),
    ]