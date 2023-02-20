# Generated by Django 4.0.3 on 2022-04-24 06:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('completed', models.BooleanField(default=False)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.customer')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Cartitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.cart')),
            ],
        ),
    ]
