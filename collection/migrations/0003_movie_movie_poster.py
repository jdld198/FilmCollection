# Generated by Django 2.1.2 on 2019-03-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_shelf_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(default='collection\\static\\collection\\placeholder_poster.png', upload_to=''),
        ),
    ]
