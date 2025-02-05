# Generated by Django 5.1.3 on 2024-11-13 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_post_like_remove_post_like_count_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="like",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="post",
            name="like_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
