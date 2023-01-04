from django.db import models


class Check(models.Model):
    types = (("kitchen", "client"),)
    statuses = (
        ("new", "new"),
        ("rendered", "rendered"),
        ("printed", "printed"),
    )

    class TYPES:
        KITCHEN = "kitchen"
        CLIENT = "client"

    class STATUSES:
        NEW = "new"
        RENDERED = "rendered"
        PRINTED = "printed"

    printer = models.ForeignKey("Printer", on_delete=models.CASCADE)
    type = models.CharField(max_length=32, choices=types)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=statuses)

    class Meta:
        db_table = "check"
        verbose_name = "check"
        verbose_name_plural = "check"
        indexes = [
            models.Index(
                fields=[
                    "type",
                ]
            ),
            models.Index(
                fields=[
                    "status",
                ]
            ),
        ]
