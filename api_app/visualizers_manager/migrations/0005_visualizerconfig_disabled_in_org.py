# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-06 10:38

from django.db import migrations, models


def migrate_disabled_config(apps, schema_editor):
    VisualizerConfig = apps.get_model("visualizers_manager", "VisualizerConfig")
    OrganizationPluginState = apps.get_model("api_app", "OrganizationPluginState")
    for plugin_state in OrganizationPluginState.objects.filter(type="3", disabled=True):
        config = VisualizerConfig.objects.get(name=plugin_state.plugin_name)
        config.disabled_in_organizations.add(plugin_state.organization)


def backwards_migrate_disabled_config(apps, schema_editor):
    VisualizerConfig = apps.get_model("visualizers_manager", "VisualizerConfig")
    OrganizationPluginState = apps.get_model("api_app", "OrganizationPluginState")
    for config in VisualizerConfig.objects.all():
        for org in config.disabled_in_organizations.all():
            OrganizationPluginState.objects.create(
                plugin_name=config.name, type="3", organization=org, disabled=True
            )


class Migration(migrations.Migration):

    dependencies = [
        ("certego_saas_organization", "0001_initial"),
        ("visualizers_manager", "0004_alter_visualizerreport_report"),
    ]

    operations = [
        migrations.AddField(
            model_name="visualizerconfig",
            name="disabled_in_organizations",
            field=models.ManyToManyField(
                blank=True,
                related_name="visualizers_manager_visualizerconfig_disabled",
                to="certego_saas_organization.Organization",
            ),
        ),
        migrations.RunPython(
            migrate_disabled_config, backwards_migrate_disabled_config
        ),
    ]
