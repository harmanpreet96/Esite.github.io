# Generated by Django 2.2.5 on 2020-08-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myagri', '0006_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=''),
        ),
    ]
