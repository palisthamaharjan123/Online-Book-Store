# Generated by Django 4.0.3 on 2022-04-07 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_book_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='name',
            new_name='rname',
        ),
        migrations.RemoveField(
            model_name='request',
            name='customer',
        ),
    ]