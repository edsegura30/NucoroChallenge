# Pip imports
from django.db import models

# Internal imports
from data_providers.constants import ProviderApplicationTypes


class DataProviderManager(models.Manager):
    def active(self):
        return super().get_queryset().filter(active=True)


class DataProvider(models.Model):
    active = models.BooleanField()
    adapter = models.CharField(
        choices=ProviderApplicationTypes.get_choices(),
        max_length=20
    )
    name = models.CharField(db_index=True, max_length=140)
    priority = models.PositiveIntegerField(db_index=True)

    objects = DataProviderManager

    class Meta:
        ordering = ["priority"]

    def __str__(self):
        return f'{self.name} ({self.adapter})'
