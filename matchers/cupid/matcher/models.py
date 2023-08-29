from django.db import models
# from .algorithm.cupid import Cupid
# from .algorithm.data_sources.csv.csv_table import CSVTable


class Matcher(models.Model):
    """
    The model that represents a schema-matching algorithm
    """
    source_schema = models.CharField(max_length=100, blank=True, default='')
    target_schema = models.CharField(max_length=100, blank=True, default='')

    @staticmethod
    def match_schemas(data):
        # # TODO matcher implementation
        # matcher = Cupid()
        # source_schema = CSVTable(data['source_schema'], 'source_schema')
        # target_schema = CSVTable(data['target_schema'], 'target_schema')
        # matches = matcher.get_matches(source_schema, target_schema).items()
        # # Sort results by similarity score, descending
        # sorted_matches = sorted(matches,
        #                       key=lambda item: item[1], reverse=True)
        # matches_response = list(map(Matcher.build_match_response, sorted_matches))

        return []
    
    @staticmethod
    def build_match_response(match):
        return {
            'source_element': match[0][0][1],
            'target_element': match[0][1][1],
            'score': match[1]
        }

class MatcherResponse(models.Model):
    """
    The model that represents the results of a schema-matching algorithm
    """
    source_element = models.CharField(max_length=100, blank=True, default='')
    target_element = models.CharField(max_length=100, blank=True, default='')
    score = models.DecimalField(max_digits=4, decimal_places=3)
