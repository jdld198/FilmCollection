# Generated by Django 2.1.2 on 2019-03-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0007_auto_20190322_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_poster',
            field=models.TextField(null=True),
        ),
    ]
