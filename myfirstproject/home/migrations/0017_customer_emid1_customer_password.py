# Generated by Django 4.1.7 on 2023-05-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_customer_id_customer_address_alter_customer_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='EMid1',
            field=models.IntegerField(null=True),
        ),
       
    ]
