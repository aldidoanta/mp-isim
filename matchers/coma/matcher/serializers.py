from rest_framework import serializers
from matcher.models import Matcher


class MatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matcher
        fields = ['source_schema', 'target_schema']
    source_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)
    target_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)
