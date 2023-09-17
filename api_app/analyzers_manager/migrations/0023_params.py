# Generated by Django 4.1.7 on 2023-04-05 15:22

from django.db import migrations


def create_config(configs, _type: str, Parameter, PluginConfig):
    for config in configs:
        for param_name, param_values in config.params.items():
            param = Parameter(
                analyzer_config=config,
                name=param_name,
                type=param_values["type"],
                description=param_values["description"],
                is_secret=False,
                required=param_values.get("required", False),
            )
            param.full_clean()
            param.save()
            if "default" in param_values:
                if param_values["default"] is None and param_values["type"] == "str":
                    param_values["default"] = ""
                PluginConfig.objects.get_or_create(
                    owner=None,
                    value=param_values["default"],
                    plugin_name=config.name,
                    attribute=param_name,
                    type=_type,
                    config_type="1",
                )
        for secret_name, secret_values in config.secrets.items():
            secret = Parameter(
                analyzer_config=config,
                name=secret_name,
                type=secret_values["type"],
                description=secret_values["description"],
                is_secret=True,
                required=secret_values["required"],
            )
            secret.full_clean()
            secret.save()

            if "default" in secret_values:
                PluginConfig.objects.get_or_create(
                    owner=None,
                    value=secret_values["default"],
                    plugin_name=config.name,
                    attribute=secret_name,
                    type=_type,
                    config_type="2",
                )


def migrate(apps, schema_editor):
    AnalyzerConfig = apps.get_model("analyzers_manager", "AnalyzerConfig")
    Parameter = apps.get_model("api_app", "Parameter")
    PluginConfig = apps.get_model("api_app", "PluginConfig")
    create_config(list(AnalyzerConfig.objects.all()), "1", Parameter, PluginConfig)


def reverse_migrate(apps, schema_editor):
    AnalyzerConfig = apps.get_model("analyzers_manager", "AnalyzerConfig")
    PluginConfig = apps.get_model("api_app", "PluginConfig")
    for config in AnalyzerConfig.objects.all():
        config.params = {}
        config.secrets = {}

        for parameter in config.parameters.all():
            if parameter.is_secret:
                config.secrets[parameter.name] = {
                    "description": parameter.description,
                    "required": parameter.required,
                    "type": parameter.type,
                }
                try:
                    value = PluginConfig.objects.get(
                        plugin_name=config.name,
                        attribute=parameter.name,
                        config_type="2",
                        owner__isnull=True,
                        organization=None,
                        type="1",
                    )
                except PluginConfig.DoesNotExist:
                    ...
                else:
                    config.secrets[parameter.name]["default"] = value.value
                    value.delete()

            else:
                value = PluginConfig.objects.get(
                    plugin_name=config.name,
                    attribute=parameter.name,
                    config_type="1",
                    owner__isnull=True,
                    organization=None,
                    type="1",
                )
                config.params[parameter.name] = {
                    "default": value.value,
                    "type": parameter.type,
                    "description": parameter.description,
                }
                value.delete()
            config.full_clean()
            config.save()


class Migration(migrations.Migration):

    dependencies = [
        ("analyzers_manager", "0022_otx_check_hash_timeout"),
        ("api_app", "0027_parameter"),
    ]

    operations = [
        migrations.RunPython(migrate, reverse_migrate),
        migrations.RemoveField(model_name="analyzerconfig", name="params"),
        migrations.RemoveField(model_name="analyzerconfig", name="secrets"),
    ]
