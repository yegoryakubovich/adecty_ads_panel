from datetime import timedelta, datetime

from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Session, Message, Sleep, SleepStates


@admin.register(Session, site=admin_site)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "id", "phone", "username", "first_name", "last_name", "country", "shop", "tg_user_id", "state", "created",
        "message_send_now", "sleep_now", "work"
    )
    list_filter = ("state", "work")
    readonly_fields = ("id", "phone", "tg_user_id", "created")
    list_per_page = 1000

    # search_fields = ()
    # list_editable = ()

    def has_add_permission(self, request):
        return False

    @admin.display(description="Сообщений")
    def message_send_now(self, model: Session):
        return len(Message.objects.filter(session=model).all())

    @admin.display(description="Сон")
    def sleep_now(self, model: Session):
        sleep = Sleep.objects.filter(session=model, state=SleepStates.enable).first()
        if sleep:
            delta = (sleep.created + timedelta(seconds=sleep.time_second)).replace(tzinfo=None) - datetime.utcnow()
            return f"{delta}"
        return f"Нет"
