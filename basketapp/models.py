from django.db import models
from django.conf import settings
from mainapp.models import Accommodation


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket')
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    staying = models.PositiveIntegerField(verbose_name='сутки', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)