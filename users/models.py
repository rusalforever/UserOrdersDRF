from django.db import models
from django.utils import timezone


class User(models.Model):
    # user = models.ForeignKey(User, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_registration = models.DateField(default=timezone.now)
    date_birthday = models.DateField(null=True)

    class Meta:
        unique_together = ("first_name", "last_name", "date_birthday")

    def __str__(self):
        return self.first_name + ' ' + self.last_name
