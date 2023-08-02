# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from typing import Any
from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models


@admin.register(models.BuildServer)
class BuildServerAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_editable = ['description']


@admin.register(models.BuildInfo)
class BuildInfoAdmin(admin.ModelAdmin):
    list_display = ['build_server', 'build', 'job',
                    'output_paths_count', 'downloadables_count']
    list_select_related = ['build_server']

    @admin.display(ordering='output_paths_count')
    def output_paths_count(self, buildinfo):
        url = (
            reverse("admin:buildinfo_outputstorepath_changelist")
            + '?'
            + urlencode({
                'buildinfo__id': str(buildinfo.id)
            }))
        return format_html(f'<a href="{url}">{buildinfo.output_paths_count}</a>')

    @admin.display(ordering='downloadables_count')
    def downloadables_count(self, buildinfo):
        url = (
            reverse("admin:buildinfo_downloadable_changelist")
            + '?'
            + urlencode({
                'buildinfo__id': str(buildinfo.id)
            }))
        return format_html(f'<a href="{url}">{buildinfo.downloadables_count}</a>')

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(downloadables_count=Count('downloadables'), output_paths_count=Count('output_store_paths'))


@admin.register(models.OutputStorePath)
class OutputStorePathAdmin(admin.ModelAdmin):
    list_display = ['buildinfo', 'path']
    list_select_related = ['buildinfo']


@admin.register(models.Downloadable)
class DownloadableAdmin(admin.ModelAdmin):
    list_display = ['buildinfo', 'file_type', 'file_name']
    list_select_related = ['buildinfo']
