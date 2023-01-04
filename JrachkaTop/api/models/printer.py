from uuid import uuid4

from django.db import models

# Create your models here.


class Printer(models.Model):
    types = (
        ("kitchen", "kitchen"),
        ("client", "client"),
    )

    id = models.UUIDField(primary_key=True, default=uuid4)
    api_key = models.CharField(max_length=255)
    check_type = models.CharField(max_length=32, choices=types)
    point_id = models.ForeignKey("point", on_delete=models.CASCADE)

    class Meta:
        db_table = "printer"
        verbose_name = "printer"
        verbose_name_plural = "printer"
