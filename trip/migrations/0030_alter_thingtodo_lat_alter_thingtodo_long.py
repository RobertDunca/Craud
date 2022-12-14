# Generated by Django 4.0.6 on 2022-10-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0029_alter_thingtodo_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thingtodo',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='thingtodo',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True),
        ),
    ]
