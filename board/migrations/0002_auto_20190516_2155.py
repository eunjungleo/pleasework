# Generated by Django 2.2.1 on 2019-05-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='board',
            name='cover',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
