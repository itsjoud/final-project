# Generated by Django 4.1.7 on 2023-05-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_product_pic'),
    ]

    operations = [
    
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='SSBN',
            field=models.IntegerField(null=True),
        ),
    ]