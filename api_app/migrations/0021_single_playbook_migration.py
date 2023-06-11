# This file is a part of IntelOwl https://github.com/intelowlproject/IntelOwl
# See the file 'LICENSE' for copying permission.

# Generated by Django 3.2.18 on 2023-03-07 08:29

from django.db import migrations


def migrate_playbooks(apps, schema_editor):
    Job = apps.get_model("api_app", "Job")
    for job in Job.objects.all():
        start_pk = job.pk
        if not job.playbooks_to_execute.exists():
            continue
        for p in job.playbooks_to_execute.all():
            job.pk = None
            job.playbook_requested = p
            job.playbook_to_execute = p
            job.save()
            starter_job = Job.objects.get(pk=start_pk)
            starter_job.analyzerreports.filter(parent_playbook=p).update(job=job)
            starter_job.connectorreports.filter(parent_playbook=p).update(job=job)
            starter_job.visualizerreports.filter(parent_playbook=p).update(job=job)
        starter_job = Job.objects.get(pk=start_pk)
        starter_job.delete()


def reverse_migrate_playbooks(apps, schema_editor):
    Job = apps.get_model("api_app", "Job")
    for job in Job.objects.all():
        if job.playbook_to_execute:
            job.playbooks_to_execute.set([job.playbook_to_execute])
        if job.playbook_requested:
            job.playbooks_requested.set([job.playbook_requested])


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0020_single_playbook_pre_migration'),
        ("analyzers_manager", "00011_vt_url_subpath"),
        ("connectors_manager", "0009_parent_playbook_foreign_key"),
        ("visualizers_manager", "0008_parent_playbook_foreign_key"),
    ]

    operations = [
        migrations.RunPython(
            migrate_playbooks, reverse_migrate_playbooks
        ),

    ]
