# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-07 08:29

from django.db import migrations, models


def migrate(apps, schema_editor):
    PlaybookConfig = apps.get_model("playbooks_manager", "PlaybookConfig")
    AnalyzerConfig = apps.get_model("analyzers_manager", "AnalyzerConfig")
    ConnectorConfig = apps.get_model("connectors_manager", "ConnectorConfig")
    VisualizerConfig = apps.get_model("visualizers_manager", "VisualizerConfig")
    Job = apps.get_model("api_app", "Job")
    for job in Job.objects.all():
        job.analyzers2_requested.set(AnalyzerConfig.objects.filter(name__in=job.analyzers_requested))
        job.analyzers2_to_execute.set(AnalyzerConfig.objects.filter(name__in=job.analyzers_to_execute))

        job.connectors2_requested.set(ConnectorConfig.objects.filter(name__in=job.connectors_requested))
        job.connectors2_to_execute.set(ConnectorConfig.objects.filter(name__in=job.connectors_to_execute))

        job.visualizers2_to_execute.set(VisualizerConfig.objects.filter(name__in=job.visualizers_to_execute))


        job.playbooks2_requested.set(PlaybookConfig.objects.filter(name__in=job.playbooks_requested))
        job.playbooks2_to_execute.set(PlaybookConfig.objects.filter(name__in=job.playbooks_to_execute))
        job.full_clean()
        job.save()

def reverse_migrate(apps, schema_editor):
    Job = apps.get_model("api_app", "Job")
    for job in Job.objects.all():
        job.analyzers_requested=list(job.analyzers2_requested.all().values_list("name", flat=True))
        job.analyzers_to_execute=list(job.analyzers2_to_execute.all().values_list("name", flat=True))

        job.connectors_requested=list(job.connectors2_requested.all().values_list("name", flat=True))
        job.connectors_to_execute=list(job.connectors2_to_execute.all().values_list("name", flat=True))

        job.visualizers_to_execute=list(job.visualizers2_to_execute.all().values_list("name", flat=True))


        job.playbooks_requested=list(job.playbooks2_requested.all().values_list("name", flat=True))
        job.playbooks_to_execute=list(job.playbooks2_to_execute.all().values_list("name", flat=True))

        job.full_clean()
        job.save()

class Migration(migrations.Migration):

    dependencies = [
        ('playbooks_manager', '0004_datamigration'),
        ('analyzers_manager', '0006_analyzerconfig_disabled_in_org'),
        ('visualizers_manager', '0005_visualizerconfig_disabled_in_org'),
        ('connectors_manager', '0006_connectorconfig_disabled_in_org'),
        ('api_app', '0018_tag_validation'),
    ]

    operations = [

        migrations.AddField(
            model_name='job',
            name='analyzers2_requested',
            field=models.ManyToManyField(blank=True, related_name='requested_in_jobs', to='analyzers_manager.AnalyzerConfig'),
        ),
        migrations.AddField(
            model_name='job',
            name='analyzers2_to_execute',
            field=models.ManyToManyField(blank=True, related_name='executed_in_jobs',
                                         to='analyzers_manager.AnalyzerConfig'),
        ),
        migrations.AddField(
            model_name='job',
            name='connectors2_requested',
            field=models.ManyToManyField(blank=True, related_name='requested_in_jobs',
                                         to='connectors_manager.ConnectorConfig'),
        ),
        migrations.AddField(
            model_name='job',
            name='connectors2_to_execute',
            field=models.ManyToManyField(blank=True, related_name='executed_in_jobs',
                                         to='connectors_manager.ConnectorConfig'),
        ),
        migrations.AddField(
            model_name='job',
            name='playbooks2_requested',
            field=models.ManyToManyField(blank=True, related_name='requested_in_jobs',
                                         to='playbooks_manager.PlaybookConfig'),
        ),
        migrations.AddField(
            model_name='job',
            name='playbooks2_to_execute',
            field=models.ManyToManyField(blank=True, related_name='executed_in_jobs',
                                         to='playbooks_manager.PlaybookConfig'),
        ),
        migrations.AddField(
            model_name='job',
            name='visualizers2_to_execute',
            field=models.ManyToManyField(blank=True, related_name='executed_in_jobs',
                                         to='visualizers_manager.VisualizerConfig'),
        ),
        migrations.RunPython(
            migrate, reverse_migrate
        ),
        migrations.RemoveField(
            model_name='job',
            name='analyzers_to_execute',
        ),
        migrations.RemoveField(
            model_name='job',
            name='analyzers_requested',
        ),
        migrations.RemoveField(
            model_name='job',
            name='connectors_requested',
        ),

        migrations.RemoveField(
            model_name='job',
            name='connectors_to_execute',
        ),

        migrations.RemoveField(
            model_name='job',
            name='playbooks_requested',
        ),

        migrations.RemoveField(
            model_name='job',
            name='playbooks_to_execute',
        ),

        migrations.RemoveField(
            model_name='job',
            name='visualizers_to_execute',
        ),
        migrations.RenameField(
            model_name="job",
            old_name="analyzers2_to_execute",
            new_name="analyzers_to_execute"
        ),
        migrations.RenameField(
            model_name='job',
            old_name='analyzers2_requested',
            new_name="analyzers_requested"
        ),
        migrations.RenameField(
            model_name='job',
            old_name='connectors2_requested',
            new_name="connectors_requested"
        ),

        migrations.RenameField(
            model_name='job',
            old_name='connectors2_to_execute',
            new_name="connectors_to_execute"
        ),

        migrations.RenameField(
            model_name='job',
            old_name='playbooks2_requested',
            new_name="playbooks_requested"
        ),

        migrations.RenameField(
            model_name='job',
            old_name='playbooks2_to_execute',
            new_name="playbooks_to_execute"
        ),

        migrations.RenameField(
            model_name='job',
            old_name='visualizers2_to_execute',
            new_name="visualizers_to_execute"
        ),

    ]
