# Generated by Django 4.0.3 on 2022-04-29 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_order_cartitem_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cartItem_Id',
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]