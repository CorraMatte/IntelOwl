# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.16 on 2022-12-27 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playbooks_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cachedplaybook",
            name="job",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="job",
                to="api_app.job",
            ),
        ),
    ]