from uuid import uuid4

from django.db import models
from names import get_full_name

# Create your models here.


def get_unique_name():
    point_name = True
    while point_name:
        name = get_full_name()
        point_name = Point.objects.filter(name=name)
        if not point_name:
            return name


class Point(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(
        max_length=64, unique=True, null=False, default=get_unique_name
    )
    api_key = models.CharField(max_length=255)

    class Meta:
        db_table = "point"
        verbose_name = "point"
        verbose_name_plural = "point"
        indexes = [models.Index(fields=["name", "id"])]
