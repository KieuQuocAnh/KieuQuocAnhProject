# Generated by Django 5.1.3 on 2024-11-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_like_post_like_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="comment",
            field=models.TextField(blank=True, default="None"),
        ),
    ]
