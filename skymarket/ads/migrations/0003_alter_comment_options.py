# Generated by Django 3.2.6 on 2023-01-15 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
