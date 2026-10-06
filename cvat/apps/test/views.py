# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cvat.apps.engine.models import Job, Label, LabeledShape, Task


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def annotation_counts(request, task_id):
    """
    Return annotation count per class label for the given task.

    K1: This view (views.py in cvat.apps.test) computes the count.
    We query LabeledShape, group by label, and count rows.
    LabeledShape is the model that stores each annotated shape (rectangle,
    polygon, etc.) on a frame. Each shape has a FK to Label which carries
    the human-readable name.

    K2: Label model (cvat/apps/engine/models.py) has a `name` field.
    Path: Task -> Job -> LabeledShape.label -> Label.name
    """

    # --- permission check: does the task exist and can this user see it? ---
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response(
            {"detail": f"Task {task_id} not found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    # Check that at least one job in this task is accessible to the user.
    # CVAT uses Job-level assignees; superusers can see everything.
    jobs = Job.objects.filter(segment__task=task)
    if not request.user.is_superuser:
        jobs = jobs.filter(assignee=request.user)
        if not jobs.exists():
            return Response(
                {"detail": "You do not have access to this task."},
                status=status.HTTP_403_FORBIDDEN,
            )

    # --- count shapes per label for this task ---
    counts = (
        LabeledShape.objects.filter(job__segment__task=task)
        .values("label__name")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    # Build the response payload
    data = [
        {"label": row["label__name"], "count": row["count"]}
        for row in counts
    ]

    return Response(
        {
            "task_id": task_id,
            "task_name": task.name,
            "annotation_counts": data,
        }
    )
