# Generated by Django 4.0.3 on 2022-04-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_alter_cart_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Customer',
            new_name='user',
        ),
    ]
