# Generated by Django 5.0.4 on 2024-05-12 10:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='promo_coupon',
            name='discount_in_percents',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
