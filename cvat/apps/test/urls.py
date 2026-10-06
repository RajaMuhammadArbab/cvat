# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path

from . import views

urlpatterns = [
    path(
        "tasks/<int:task_id>/annotation-counts",
        views.annotation_counts,
        name="annotation-counts",
    ),
]
