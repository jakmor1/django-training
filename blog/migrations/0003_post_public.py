# Generated by Django 4.1.7 on 2023-03-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
