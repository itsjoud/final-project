# Generated by Django 4.1.7 on 2023-05-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_customer_emid1_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
    ]