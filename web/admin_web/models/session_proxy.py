from django.db import models

from admin_web.models import Session, Proxy


class SessionProxy(models.Model):
    class Meta:
        db_table = 'session_proxy'
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(default=False, verbose_name="Время создания")

    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name="Состояние",
                                related_name="session_proxy_session")
    proxy = models.ForeignKey(Proxy, on_delete=models.CASCADE, verbose_name="Состояние",
                              related_name="session_proxy_proxy")

    def __str__(self):
        return f"{self.session}-{self.proxy} ({self.id})"
