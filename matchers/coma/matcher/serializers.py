from rest_framework import serializers
from matcher.models import Matcher


class MatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matcher
        fields = ['dataprovider_schema', 'dataconsumer_schema']
    dataprovider_schema = serializers.CharField(required=False, allow_blank=True, max_length=100)
    dataconsumer_schema = serializers.CharField(required=False, allow_blank=True, max_length=100)
