# Generated by Django 4.0.4 on 2022-06-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elib', '0002_book_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_des',
            field=models.TextField(),
        ),
    ]
