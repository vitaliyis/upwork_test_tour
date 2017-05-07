from django.db import models


class Tour(models.Model):
    name = models.CharField(max_length=256, blank=False)
    country = models.CharField(max_length=256, blank=False)
    city = models.CharField(max_length=128, blank=False)
    hotel = models.CharField(max_length=256, blank=False)
    start = models.DateField()
    finish = models.DateField()
    quantity_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "%s (%s) %s :: %s" % (self.name, self.country, self.start, self.finish)