from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Proxy, Session, SessionProxy


@admin.register(Proxy, site=admin_site)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ("id", "country", "ip_port", "user", "password", "type", "state", "created", "session_count")
    list_filter = ("state", "type")
    readonly_fields = ("id", "created")

    # search_fields = ()
    # list_editable = ()

    def has_add_permission(self, request):
        return False

    @admin.display(description="ip:port")
    def ip_port(self, model: Proxy):
        return f"{model.host}:{model.port}"

    @admin.display(description="Сессий")
    def session_count(self, model: Proxy):
        return f"{len(SessionProxy.objects.filter(proxy=model).all())}/{model.max_link}"
