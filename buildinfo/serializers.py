# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from rest_framework import serializers
from .models import BuildInfo, BuildServer, OutputStorePath, Downloadable


class BuildServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildServer
        fields = ['id', 'name', 'description']


class OutputStorePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputStorePath
        fields = ['id', 'buildinfo', 'path']


class DownloadableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downloadable
        fields = ['id', 'buildinfo', 'file_type', 'file_name']


class BuildinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildInfo
        fields = ['id', 'created', 'project', 'jobset', 'job', 'build',
                  'system', 'nix_name', 'queued_at', 'build_started',
                  'build_finished', 'post_processing_done', 'derivation_store_path',
                  'closure_size', 'output_size', 'build_server']


class BuildinfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildInfo
        fields = ['id', 'build_server',
                  'build', 'job', 'build_finished']
