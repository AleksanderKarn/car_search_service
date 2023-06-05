from django.db import models

from locations.models import Location


class Cargo(models.Model):
    pick_up = models.ForeignKey(Location, on_delete=models.PROTECT, verbose_name='Локация', related_name='pick_up')
    delivery = models.ForeignKey(Location, on_delete=models.PROTECT, verbose_name='Локация', related_name='delivery')
    weight = models.IntegerField(verbose_name='Вес')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'Груз: {self.description}, вес {self.weight} - доставить от {self.pick_up} до {self.delivery}'

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'
