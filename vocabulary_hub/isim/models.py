import requests
from django.conf import settings
from django.db import models
from typing import Dict, List

MATCHERS = [
    ('coma', 'COMA'),
    ('cupid', 'Cupid'),
    ('dummy', 'Dummy'),
]

MATCHER_HOSTS = {
    'coma': settings.MATCHER_COMA_HOST,
    'cupid': None,
    'dummy': settings.MATCHER_DUMMY_HOST,
}


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
            r = requests.post(f'{MATCHER_HOSTS[data["matcher"]]}/matcher/match-schemas',
                              json=matcher_request_body)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
        source_elements = filter(None, data['source_schema'].split(',')) # use filter() to remove empty strings
        target_elements = filter(None, data['target_schema'].split(','))
        matched_elements = r.json()

        # TODO proper HTTP 5xx error handling
        response = {
            'matched_elements': matched_elements,
            'unmatched_elements': Isim.get_unmatched_elements(source_elements, target_elements, matched_elements),
            'matcher': data['matcher'],
        }
        # Simple price calculation based on the number of intervals and price per interval
        if 'pricing_info' in data:
            response['total_price'] = data['pricing_info']['intervals'] * data['pricing_info']['price_per_interval']
        return response
    
    @staticmethod
    def get_unmatched_elements(source_elements: List[str], 
                               target_elements: List[str], 
                               matched_elements: any) -> Dict[str,str]:
        matched_source_elements = list()
        matched_target_elements = list()

        # create a list of matched source elements and matched target elements
        if (matched_elements):
            matched_source_elements = [element['source_element'] for element in matched_elements]
            matched_target_elements = [element['target_element'] for element in matched_elements]

        # use `str` instead of `List[str]` because Mendix (the frontend) doesn't support array of literals
        unmatched_elements = {
            'source_elements': ','.join(set(source_elements) - set(matched_source_elements)),
            'target_elements': ','.join(set(target_elements) - set(matched_target_elements))
        }

        # find the differences
        return unmatched_elements
