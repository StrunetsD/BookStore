# Generated by Django 5.1.3 on 2024-11-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
