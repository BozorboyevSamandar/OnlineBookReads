# Generated by Django 4.1.3 on 2022-11-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(default='default-book.jpg', upload_to=''),
        ),
    ]
