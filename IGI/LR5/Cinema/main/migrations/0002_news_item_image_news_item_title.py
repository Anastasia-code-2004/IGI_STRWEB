# Generated by Django 5.0.4 on 2024-05-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_item',
            name='image',
            field=models.ImageField(default='cinema.jpg', upload_to='images'),
        ),
        migrations.AddField(
            model_name='news_item',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
