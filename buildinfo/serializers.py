# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from rest_framework import serializers
from .models import BuildInfo, BuildServer, OutputStorePath, Downloadable


class BuildServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildServer
        fields = ['id', 'name', 'description']


class BuildinfoBuildServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildServer
        fields = ['id', 'name']


class DownloadableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downloadable
        fields = ['id', 'buildinfo', 'file_type', 'file_name']


class DownloadableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downloadable
        fields = ['id', 'file_name']


class BuildinfoDownloadableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Downloadable
        fields = ['id', 'file_type', 'file_name']

    def create(self, validated_data):
        buildinfo_id = self.context['kwargs']['buildinfo_pk']
        return Downloadable.objects.create(buildinfo_id=buildinfo_id, **validated_data)


class BuildinfoOutputStorePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputStorePath
        fields = ['id', 'path']

    def create(self, validated_data):
        buildinfo_id = self.context['kwargs']['buildinfo_pk']
        return OutputStorePath.objects.create(buildinfo_id=buildinfo_id, **validated_data)


class BuildinfoSerializer(serializers.ModelSerializer):
    build_server = BuildinfoBuildServerSerializer(read_only=True)
    output_store_paths = BuildinfoOutputStorePathSerializer(
        many=True, read_only=True)
    downloadables = BuildinfoDownloadableSerializer(many=True, read_only=True)

    class Meta:
        model = BuildInfo
        fields = ['id', 'created', 'build_server', 'build', 'project', 'jobset', 'job',
                  'system', 'nix_name', 'queued_at', 'build_started',
                  'build_finished', 'post_processing_done', 'derivation_store_path', 'output_store_paths',
                  'closure_size', 'output_size', 'downloadables']


class CreateBuildinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildInfo
        fields = ['id', 'created', 'build_server', 'build', 'project', 'jobset', 'job',
                  'system', 'nix_name', 'queued_at', 'build_started',
                  'build_finished', 'post_processing_done', 'derivation_store_path',
                  'closure_size', 'output_size']


class BuildinfoListSerializer(serializers.ModelSerializer):
    build_server = serializers.StringRelatedField()

    class Meta:
        model = BuildInfo
        fields = ['id', 'build_server',
                  'build', 'target', 'system', 'build_finished']

    target = serializers.SerializerMethodField(method_name='target_from_job')

    def target_from_job(self, buildinfo: BuildInfo):
        return buildinfo.job.split('.')[0]
