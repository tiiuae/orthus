# SPDX-FileCopyrightText: 2023 Technology Innovation Institute (TII)
# SPDX-License-Identifier: Apache-2.0

from django.urls import path
from . import views

urlpatterns = [
    path('buildinfo/', views.buildinfo_list),
    # path('buildinfo/<str:server>/<int:build_id>/', views.build_detail),
    path('buildinfo/<int:pk>/', views.buildinfo_detail),
    path('output_store_path/', views.output_store_path_list),
    path('output_store_path/<int:pk>/', views.output_store_path_detail),
    path('downloadable/', views.downloadable_list),
    path('downloadable/<int:pk>/', views.downloadable_detail),
]
