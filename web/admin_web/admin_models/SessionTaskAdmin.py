from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import SessionTask


@admin.register(SessionTask, site=admin_site)
class SessionTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "session", "group", "order", "message", "state", "type", "created")
    list_filter = ("state", "type")
    readonly_fields = ("id", "created")

    # search_fields = ()
    # list_editable = ()

    def has_add_permission(self, request):
        return False