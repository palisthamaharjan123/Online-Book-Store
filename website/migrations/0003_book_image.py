# Generated by Django 4.0.3 on 2022-04-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_book_author_book_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to='static\\website\\imh'),
        ),
    ]
