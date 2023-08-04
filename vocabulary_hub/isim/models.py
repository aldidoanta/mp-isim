from django.db import models

MATCHERS = [
    ('coma', 'COMA'),
    ('cupid', 'Cupid'),
]


class PricingInfo(models.Model):
    """
    The model that represents pricing information of the provided data from Data Provider.
    """
    intervals = models.IntegerField
    price_per_interval = models.IntegerField

class Isim(models.Model):
    """
    The model that represents an interoperability scenario.
    """
    created = models.DateTimeField(auto_now_add=True)
    dataprovider_schema = models.CharField(max_length=100, blank=True, default='')
    dataconsumer_schema = models.CharField(max_length=100, blank=True, default='')
    matcher = models.CharField(choices=MATCHERS, default=MATCHERS[0], max_length=100)
    pricing_info = PricingInfo()

    class Meta:
        ordering = ['created']

    @staticmethod
    def simulate(data):
        return {
            'merged_schema': data['dataprovider_schema'] + ' ' + data['dataconsumer_schema'],
            'matcher': data['matcher'],
            'total_price': data['pricing_info']['intervals'] * data['pricing_info']['price_per_interval'],
        }
