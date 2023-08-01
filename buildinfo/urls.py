# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('buildinfo', views.BuildinfoViewset)
router.register('output_store_path', views.OutputStorePathViewset)
router.register('downloadable', views.DownloadableViewset)

urlpatterns = [
    path('', include(router.urls)),
]
