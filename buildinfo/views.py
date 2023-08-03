# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from pprint import pprint
from rest_framework.viewsets import ModelViewSet
from .models import BuildInfo, OutputStorePath, Downloadable
from .serializers import *


class BuildServerViewSet(ModelViewSet):
    queryset = BuildServer.objects.all()
    serializer_class = BuildServerSerializer


class BuildinfoViewSet(ModelViewSet):
    queryset = BuildInfo.objects.prefetch_related(
        'output_store_paths').prefetch_related('downloadables').all()
    serializer_class = BuildinfoSerializer

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('many') == True:
            return BuildinfoListSerializer(*args, **kwargs)
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return CreateBuildinfoSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request, 'kwargs': self.kwargs}


class BuildinfoStorePathViewSet(ModelViewSet):
    serializer_class = BuildinfoOutputStorePathSerializer

    def get_queryset(self):
        queryset = OutputStorePath.objects.filter(
            buildinfo_id=self.kwargs['buildinfo_pk'])
        return queryset

    def get_serializer_context(self):
        return {'request': self.request, 'kwargs': self.kwargs}


class BuildinfoDownloadableViewSet(ModelViewSet):
    serializer_class = BuildinfoDownloadableSerializer

    def get_queryset(self):
        queryset = Downloadable.objects.filter(
            buildinfo_id=self.kwargs['buildinfo_pk'])
        return queryset

    def get_serializer_context(self):
        return {'request': self.request, 'kwargs': self.kwargs}


class DownloadableViewSet(ModelViewSet):
    queryset = Downloadable.objects.all()
    serializer_class = DownloadableSerializer

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('many') == True:
            return DownloadableListSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request, 'kwargs': self.kwargs}
