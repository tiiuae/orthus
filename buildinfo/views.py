# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BuildInfo, OutputStorePath, Downloadable
from .serializers import BuildinfoSerializer, BuildinfoListSerializer, OutputStorePathSerializer, DownloadableSerializer


@api_view(['GET', 'POST'])
def buildinfo_list(request):
    queryset = BuildInfo.objects.all()
    serializer = BuildinfoListSerializer(queryset, many=True)
    return Response(serializer.data)


# @api_view()
# def build_detail(request, server, build_id):
#    return Response(f'OK\nserver={server}\nbuild_id={build_id}')


@api_view(['GET', 'PUT', 'PATCH'])
def buildinfo_detail(request, pk):
    buildinfo = get_object_or_404(BuildInfo, pk=pk)
    serializer = BuildinfoSerializer(buildinfo)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def output_store_path_list(request):
    queryset = OutputStorePath.objects.all()
    serialzer = OutputStorePathSerializer(queryset, many=True)
    return Response(serialzer.data)


@api_view(['GET', 'PUT', 'PATCH'])
def output_store_path_detail(request, pk):
    output_store_path = get_object_or_404(OutputStorePath, pk=pk)
    serializer = OutputStorePathSerializer(output_store_path)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def downloadable_list(request):
    queryset = Downloadable.objects.all()
    serialzer = DownloadableSerializer(queryset, many=True)
    return Response(serialzer.data)


@api_view(['GET', 'PUT', 'PATCH'])
def downloadable_detail(request, pk):
    downloadable = get_object_or_404(Downloadable, pk=pk)
    serializer = DownloadableSerializer(downloadable)
    return Response(serializer.data)
