# Generated by Django 4.2.3 on 2023-10-29 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
