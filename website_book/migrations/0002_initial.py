# Generated by Django 4.0.3 on 2022-04-05 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books_name', models.CharField(max_length=50)),
                ('books_price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=550)),
                ('book_image', models.ImageField(default='', upload_to='static/website/imh')),
                ('author_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='website.author')),
            ],
        ),
        migrations.CreateModel(
            name='Custm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custm_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('passwd', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('pnumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_book', models.CharField(max_length=200)),
                ('custm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.custm')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.IntegerField(default='')),
                ('total', models.IntegerField(default=0)),
                ('order_date', models.DateField(auto_now=True)),
                ('books_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.book')),
                ('custm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.custm')),
            ],
        ),
    ]
