# Generated by Django 4.0.4 on 2022-05-18 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_rename_createa_data_book_created_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='created_data',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='updated_data',
            new_name='updated_date',
        ),
    ]