# Generated by Django 5.0.4 on 2024-05-09 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_about_company_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]
