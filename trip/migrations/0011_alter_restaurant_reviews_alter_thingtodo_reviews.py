# Generated by Django 4.0.6 on 2022-08-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0010_alter_event_photo_alter_restaurant_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='trip.review'),
        ),
        migrations.AlterField(
            model_name='thingtodo',
            name='reviews',
            field=models.ManyToManyField(blank=True, to='trip.review'),
        ),
    ]
