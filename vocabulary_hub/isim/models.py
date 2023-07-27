from django.db import models

MATCHERS = [
    ('coma', 'COMA'),
    ('cupid', 'Cupid'),
]


class Isim(models.Model):
    """
    The model that represents an interoperability scenario.
    """
    created = models.DateTimeField(auto_now_add=True)
    dataprovider_schema = models.CharField(max_length=100, blank=True, default='')
    dataconsumer_schema = models.CharField(max_length=100, blank=True, default='')
    matcher = models.CharField(choices=MATCHERS, default=MATCHERS[0], max_length=100)

    class Meta:
        ordering = ['created']
