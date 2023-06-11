# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0023_runtime_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="tlp",
            field= models.CharField(max_length=8,
                                    choices=[
                                        ("CLEAR", "Clear"),
                                        ("GREEN", "Green"),
                                        ("AMBER", "Amber"),
                                        ("RED", "Red"),
                                    ],
                                    default="CLEAR",

            )
        )

    ]
