# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('build_server', views.BuildServerViewSet)
router.register('buildinfo', views.BuildinfoViewSet)
router.register('downloadable', views.DownloadableViewSet)

output_store_path_router = routers.NestedDefaultRouter(
    router, 'buildinfo', lookup='buildinfo')
output_store_path_router.register('output_store_path',
                                  views.BuildinfoStorePathViewSet, basename='buildinfo-outputstorepath')

downloadable_router = routers.NestedDefaultRouter(
    router, 'buildinfo', lookup='buildinfo')
downloadable_router.register('downloadable',
                             views.BuildinfoDownloadableViewSet, basename='buildinfo-downloadable')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(output_store_path_router.urls)),
    path('', include(downloadable_router.urls)),
]
