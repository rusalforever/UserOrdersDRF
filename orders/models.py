from django.db import models
from django.utils import timezone

from users.models import User


class Order(models.Model):
    place = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date_created = models.DateField(default=timezone.now)
    product = models.CharField(max_length=30, blank=True)