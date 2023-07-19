from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Shop, Session, Proxy, Group, Message, MessageStates


@admin.register(Group, site=admin_site)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "state", "subscribers", "created", "delete_count")
    list_filter = ("state",)
    readonly_fields = ("id", "created")

    # search_fields = ()
    # list_editable = ()

    def has_add_permission(self, request):
        return False

    @admin.display(description="Удаленных сообщений")
    def delete_count(self, model: Group):
        messages_count = len(Message.objects.filter(group=model).all())
        delete_count = len(Message.objects.filter(group=model, state=MessageStates.deleted).all())
        return f"{delete_count}/{messages_count}"

