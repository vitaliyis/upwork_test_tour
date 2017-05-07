from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=256, blank=False)
    middle_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=False)
    country = models.CharField(max_length=128, blank=False)
    city = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False)
    phone1 = models.CharField(max_length=128, blank=False)
    phone2 = models.CharField(max_length=128, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)