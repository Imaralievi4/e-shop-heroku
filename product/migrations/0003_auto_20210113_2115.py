# Generated by Django 3.1 on 2021-01-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210113_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.UUIDField(blank=True, primary_key=True, serialize=False),
        ),
    ]
