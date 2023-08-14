from rest_framework import serializers
from matcher.models import Matcher, MatcherResponse


class MatcherRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matcher
        fields = ['source_schema', 'target_schema']
    source_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)
    target_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)

class MatcherResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatcherResponse
        fields = ['source_element', 'target_element', 'score']
    source_element = serializers.CharField(required=True, max_length=100, allow_blank=True)
    target_element = serializers.CharField(required=True, max_length=100, allow_blank=True)
    score = serializers.DecimalField(max_digits=4, decimal_places=3)
