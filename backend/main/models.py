from django.db import models


class TgUser(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'users'
