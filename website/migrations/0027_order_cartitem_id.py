# Generated by Django 4.0.3 on 2022-04-29 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_rename_cart_order_cart_id_rename_user_order_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cartItem_Id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='website.cartitems'),
        ),
    ]
