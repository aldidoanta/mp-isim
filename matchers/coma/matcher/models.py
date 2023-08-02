from django.db import models
from .algorithm.coma import Coma
from .algorithm.data_sources.csv.csv_table import CSVTable


class Matcher(models.Model):
    """
    The model that represents a schema-matching algorithm
    """
    dataprovider_schema = models.CharField(max_length=100, blank=True, default='')
    dataconsumer_schema = models.CharField(max_length=100, blank=True, default='')

    @staticmethod
    def get_matches(data):
        # Instantiate matcher and run
        # Coma requires java to be installed on your machine
        matcher = Coma(strategy="COMA_OPT")
        dataprovider_schema = CSVTable(data['dataprovider_schema'], 'dataprovider_schema')
        dataconsumer_schema = CSVTable(data['dataconsumer_schema'], 'dataconsumer_schema')
        # matcher_results = matcher.get_matches(dataprovider_schema, dataconsumer_schema).items()
        # matches = dict(sorted(matcher_results,
        #                       key=lambda item: item[1], reverse=True))
        matches = matcher.get_matches(dataprovider_schema, dataconsumer_schema).items()

        return {
            'results': matches
        }
