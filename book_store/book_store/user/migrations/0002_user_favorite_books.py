# Generated by Django 5.1.3 on 2024-11-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_review'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_books',
            field=models.ManyToManyField(blank=True, to='book.book'),
        ),
    ]