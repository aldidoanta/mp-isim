from django.db import models


class Matcher(models.Model):
    """
    The model that represents a schema-matching algorithm
    """
    dataprovider_schema = models.CharField(max_length=100, blank=True, default='')
    dataconsumer_schema = models.CharField(max_length=100, blank=True, default='')

    @staticmethod
    def get_matches(data):
        return {
            'merged_schema': data['dataprovider_schema'] + ' being matched with ' + data['dataconsumer_schema']
        }
