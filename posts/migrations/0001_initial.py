# Generated by Django 4.1.1 on 2022-09-26 09:12

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="Anonymous", max_length=15, verbose_name="Name"
                    ),
                ),
                (
                    "body",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=140,
                        null=True,
                        verbose_name="Body",
                    ),
                ),
                (
                    "image",
                    cloudinary.models.CloudinaryField(
                        blank=True, db_index=True, max_length=255, verbose_name="image"
                    ),
                ),
                (
                    "likecount",
                    models.IntegerField(
                        blank=True, default=0, verbose_name="likecount"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created DateTime"
                    ),
                ),
            ],
            options={"db_table": "post",},
        ),
    ]
