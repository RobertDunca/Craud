# Generated by Django 4.0.6 on 2022-08-05 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0011_alter_restaurant_reviews_alter_thingtodo_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]
