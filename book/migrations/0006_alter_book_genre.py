# Generated by Django 4.0.4 on 2022-04-27 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("book", "0005_book_genre")]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.CharField(
                choices=[
                    ("ROMACE", "romace"),
                    ("FANTASIES", "fantasies"),
                    ("DETECTIVE", "detective"),
                    ("ANIME", "anime"),
                ],
                max_length=90,
                null=True,
            ),
        )
    ]
