# Generated by Django 2.2.5 on 2020-08-14 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myagri', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='Price',
        ),
    ]