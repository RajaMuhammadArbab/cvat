# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.apps import AppConfig


class TestConfig(AppConfig):
    name = "cvat.apps.test"
    label = "cvat_test"
    verbose_name = "Annotation Analytics"
