# Generated by Django 4.0.6 on 2022-10-26 09:07

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0022_alter_event_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='reviews',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, null=True, to='trip.review'),
        ),
    ]