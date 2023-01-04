from django.db import models
from names import get_full_name


def get_unique_name():
    point_name = True
    while point_name:
        name = get_full_name()
        point_name = Printer.objects.filter(name=name)
        if not point_name:
            return name


class Printer(models.Model):
    types = (
        ("kitchen", "kitchen"),
        ("client", "client"),
    )

    class TYPES:
        KITCHEN = "kitchen"
        CLIENT = "client"

    name = models.CharField(
        max_length=64, unique=True, null=False, default=get_unique_name
    )
    api_key = models.CharField(max_length=255)
    check_type = models.CharField(max_length=32, choices=types)
    point_id = models.IntegerField(null=False, auto_created=True)

    class Meta:
        db_table = "printer"
        verbose_name = "printer"
        verbose_name_plural = "printer"
