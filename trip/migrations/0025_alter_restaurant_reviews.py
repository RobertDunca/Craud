# Generated by Django 4.0.6 on 2022-10-27 06:57

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0024_alter_event_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='reviews',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='trip.review'),
        ),
    ]
