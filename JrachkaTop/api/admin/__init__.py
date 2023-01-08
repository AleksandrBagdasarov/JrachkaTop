from api.admin.admin_check import CheckAdmin
from api.admin.admin_printer import PrinterAdmin
from api.models import Check, Printer, User
from django.contrib import admin

admin.site.register(User)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(Check, CheckAdmin)
