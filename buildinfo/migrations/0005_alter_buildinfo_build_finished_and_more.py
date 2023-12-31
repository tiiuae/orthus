# Generated by Django 4.2.3 on 2023-07-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildinfo', '0004_alter_buildinfo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildinfo',
            name='build_finished',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='build_started',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='closure_size',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='derivation_store_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='job',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='jobset',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='nix_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='output_size',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='post_processing_done',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='project',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='queued_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buildinfo',
            name='system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buildserver',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
