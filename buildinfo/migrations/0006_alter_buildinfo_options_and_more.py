# Generated by Django 4.2.3 on 2023-08-02 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildinfo', '0005_alter_buildinfo_build_finished_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buildinfo',
            options={'ordering': ['build_server__name', 'build']},
        ),
        migrations.RenameField(
            model_name='buildinfo',
            old_name='build_id',
            new_name='build',
        ),
    ]
