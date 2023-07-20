# Generated by Django 4.2.3 on 2023-07-20 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='company',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
