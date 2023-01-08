# Register your models here.
from api.models import Check, Printer, User
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class CheckPrinterFilter(admin.SimpleListFilter):
    title = _("Printer")

    parameter_name = "Printer"

    def lookups(self, request, model_admin):
        printer_ids = Printer.objects.values_list("id", flat=True)
        return [(x, x) for x in printer_ids]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(printer_id=self.value())
        else:
            return queryset


class CheckAdmin(admin.ModelAdmin):
    # pass
    list_display = ("check_num", "printer_id", "type", "order_id", "status")
    # list_display_links = ("printer_id",)
    list_filter = ("status", "type", CheckPrinterFilter)

    @admin.display(description="Check")
    def check_num(self, obj):
        return "Check# %s" % obj.id


admin.site.register(User)
admin.site.register(Printer)
admin.site.register(Check, CheckAdmin)
