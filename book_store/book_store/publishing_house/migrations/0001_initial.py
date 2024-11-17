# Generated by Django 5.1.3 on 2024-11-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('founded_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
