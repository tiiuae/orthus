# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from rest_framework.viewsets import ModelViewSet
from .models import BuildInfo, OutputStorePath, Downloadable
from .serializers import BuildinfoSerializer, BuildinfoListSerializer, OutputStorePathSerializer, DownloadableSerializer


class BuildinfoViewset(ModelViewSet):
    queryset = BuildInfo.objects.all()
    serializer_class = BuildinfoSerializer

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('many') == True:
            return BuildinfoListSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request}


class OutputStorePathViewset(ModelViewSet):
    queryset = OutputStorePath.objects.all()
    serializer_class = OutputStorePathSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class DownloadableViewset(ModelViewSet):
    queryset = Downloadable.objects.all()
    serializer_class = DownloadableSerializer

    def get_serializer_context(self):
        return {'request': self.request}
