from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100, verbose_name='Город')
    state_name = models.CharField(max_length=100, verbose_name='Штат')
    zip_code = models.IntegerField(verbose_name='zip-code', primary_key=True)
    lat = models.FloatField(verbose_name='Широта', default=0)
    lng = models.FloatField(verbose_name='Долгота', default=0)

    def __str__(self):
        return f'Город {self.city}, штат {self.state_name}'

    class Meta:
        verbose_name = 'локация'
        verbose_name_plural = 'локации'
