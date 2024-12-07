# Generated by Django 4.2 on 2024-12-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField(verbose_name=255)),
                ('message', models.TextField(verbose_name=255)),
            ],
        ),
    ]