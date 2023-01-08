from api.models import Printer
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class PrinterPointFilter(admin.SimpleListFilter):
    title = _("Point")

    parameter_name = "Point"

    def lookups(self, request, model_admin):
        point_ids = Printer.objects.values_list(
            "point_id", flat=True
        ).distinct()

        return [(x, x) for x in point_ids]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(point_id=self.value())
        else:
            return queryset


class PrinterAdmin(admin.ModelAdmin):
    list_display = ("printer_id", "point_id", "name", "api_key", "check_type")
    list_filter = ("id", PrinterPointFilter, "name", "check_type")

    @admin.display(description="Printer")
    def printer_id(self, obj):
        return "Printer# %s" % obj.id
