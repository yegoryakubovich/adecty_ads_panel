from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Sleep


@admin.register(Sleep, site=admin_site)
class SleepAdmin(admin.ModelAdmin):
    list_display = ("id", "session", "time_second", "state", "created")
    list_filter = ("state",)
    readonly_fields = ("id", "created")

    # search_fields = ()
    # list_editable = ()

    def has_add_permission(self, request):
        return False
