# Generated by Django 4.0.4 on 2022-06-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elib', '0003_alter_book_book_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_file',
            field=models.FileField(default=0, upload_to='book_files'),
            preserve_default=False,
        ),
    ]
