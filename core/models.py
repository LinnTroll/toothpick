from django.contrib.auth.models import User
from django.db import models


class Toothpick(models.Model):
    serial_number = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=100)
    owners = models.ManyToManyField(User, through='ToothpickOwnership')
    created_at = models.DateTimeField(auto_now_add=True)

    def actual_owners(self):
        return self.owners.filter(toothpickownership__enabled=True)

    def __str__(self):
        return self.name


class ToothpickOwnership(models.Model):
    toothpick = models.ForeignKey(Toothpick, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enabled = models.NullBooleanField(default=True)
    own_start_at = models.DateTimeField(auto_now_add=True)
    own_end_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = (
            ('toothpick', 'user', 'enabled'),
        )

    def __str__(self):
        return '{s.toothpick} {s.user}'.format(s=self)
