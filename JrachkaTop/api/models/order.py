from django.db import models


class Order(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    point_id = models.IntegerField()
    items = models.JSONField(null=False)

    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "order"
        ordering = ["id"]
