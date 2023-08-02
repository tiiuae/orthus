# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from django.db import models


class BuildServer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class BuildInfo(models.Model):
    build_server = models.ForeignKey(
        BuildServer, on_delete=models.PROTECT, related_name='build_infos')
    project = models.CharField(max_length=255, null=True, blank=True)
    jobset = models.CharField(max_length=255, null=True, blank=True)
    job = models.CharField(max_length=255, null=True, blank=True)
    build = models.IntegerField()
    system = models.CharField(max_length=255, null=True, blank=True)
    nix_name = models.CharField(max_length=255, null=True, blank=True)
    queued_at = models.DateTimeField(null=True, blank=True)
    build_started = models.DateTimeField(null=True, blank=True)
    build_finished = models.DateTimeField(null=True, blank=True)
    post_processing_done = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    derivation_store_path = models.CharField(
        max_length=255, null=True, blank=True)
    closure_size = models.FloatField(null=True, blank=True)
    output_size = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.build_server.name}-{self.build}'

    class Meta:
        ordering = ['build_server__name', 'build']


class OutputStorePath(models.Model):
    buildinfo = models.ForeignKey(
        BuildInfo, on_delete=models.CASCADE, related_name='output_store_paths')
    path = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.path

    class Meta:
        ordering = ['path']


def files_directory(instance, filename):
    return f"{instance.buildinfo.build_server.name}/{instance.buildinfo.build}/{filename}"


class Downloadable(models.Model):
    FILE_TYPE_BINARY = 'BI'
    FILE_TYPE_PROVENANCE = 'SP'
    FILE_TYPE_REPORT = 'TR'
    FILE_TYPE_LOG = 'TL'
    FILE_TYPE_SBOM = 'SB'
    FILE_TYPE_VULNSCAN = 'VS'
    FILE_TYPE_OTHER = 'OT'

    FILE_TYPES = [(FILE_TYPE_BINARY, 'Binary'),
                  (FILE_TYPE_PROVENANCE, 'SLSA Provenance'),
                  (FILE_TYPE_REPORT, 'Test Report'),
                  (FILE_TYPE_LOG, 'Test Log'),
                  (FILE_TYPE_SBOM, 'SBOM'),
                  (FILE_TYPE_VULNSCAN, 'Vulnerability Scan'),
                  (FILE_TYPE_OTHER, 'Other')]

    buildinfo = models.ForeignKey(
        BuildInfo, on_delete=models.CASCADE, related_name='downloadables')
    file_type = models.CharField(
        max_length=2, choices=FILE_TYPES, default=FILE_TYPE_OTHER)
    file_name = models.FileField(upload_to=files_directory)

    def __str__(self) -> str:
        return str(self.file_name)
