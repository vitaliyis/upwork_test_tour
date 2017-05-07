from django.db import models
from clients.models import Client
from tours.models import Tour


class StatusOrder(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField()

    def __str__(self):
        return "%s " % (self.name)


class Period(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    koef = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "%s " % (self.name)


class Order(models.Model):
    # client = models.ForeignKey(Client, blank=False, null=True)
    tour = models.ForeignKey(Tour, blank=False, null=True)
    status = models.ForeignKey(StatusOrder, blank=False, null=True)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Оплачено')
    period = models.ForeignKey(Period, blank=False, null=True)
    quantity_people = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True, default=None, verbose_name='Комментарий' )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        self.amount = self.tour.price * self.quantity_people * self.period.koef

        super(Order, self).save(*args, **kwargs)

class ClientInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    client = models.ForeignKey(Client, blank=True, null=True, default=None)


