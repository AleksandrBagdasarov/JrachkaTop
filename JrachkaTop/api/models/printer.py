from django.db import models
from uuid import uuid4

# Create your models here.


class Printer(models.Model):
    types = (
        ("kitchen", "kitchen"),
        ("client", "client"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4)
    api_key = models.CharField(max_length=255)
    check_type = models.CharField(max_length=32, choices=types)
    point_id = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "printer"
