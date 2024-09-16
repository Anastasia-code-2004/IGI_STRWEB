# Generated by Django 5.0.4 on 2024-09-14 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_delete_cart'),
        ('movies_tickets', '0007_remove_cartitem_cart_cartitem_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.client'),
        ),
    ]
