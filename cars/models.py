from django.db import models

from locations.models import Location


class Car(models.Model):
    uid = models.CharField(unique=True, max_length=5, verbose_name='Уникальный номер', primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, verbose_name='Локация')
    load_capacity = models.IntegerField(verbose_name='Грузоподъемность')

    def __str__(self):
        return f'Машина с номером {self.uid}, грузоподъемность {self.load_capacity} - локация{self.location}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
