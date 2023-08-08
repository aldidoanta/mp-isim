import requests
from django.conf import settings
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
    source_schema = models.CharField(max_length=100, blank=True, default='')
    target_schema = models.CharField(max_length=100, blank=True, default='')
    matcher = models.CharField(choices=MATCHERS, default=MATCHERS[0], max_length=100)
    pricing_info = PricingInfo()

    class Meta:
        ordering = ['created']

    @staticmethod
    def simulate(data):
        matcher_request_body = {
            'source_schema': data['source_schema'],
            'target_schema': data['target_schema'],
        }
        # API call to the selected matcher service
        try:
            r = requests.post(f'{settings.MATCHER_COMA_HOST}/matcher/get-matches',data=matcher_request_body)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
        # TODO proper HTTP 5xx error handling
        response = {
            'matches': r.json(),
            'matcher': data['matcher'],
        }
        # Simple price calculation based on the number of intervals and price per interval
        if 'pricing_info' in data:
            response['total_price'] = data['pricing_info']['intervals'] * data['pricing_info']['price_per_interval']
        return response
