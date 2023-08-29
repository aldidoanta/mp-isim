from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers
from matcher.models import Matcher, MatcherResponse


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Schemas with some matches',
            value={
                'source_schema': 'EID,Writers,Cited by,Title,Year,zipcode',
                'target_schema': 'EID,cited-by,Schrijvers,Country,postcode'
            },
            request_only=True,  # the example only applies to requests
        ),
        OpenApiExample(
            'Schemas with no matches',
            value={
                'source_schema': 'qwerty',
                'target_schema': 'defghi'
            },
            request_only=True,
        ),
    ]
)
class MatcherRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matcher
        fields = ['source_schema', 'target_schema']
    source_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)
    target_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Results with some matches',
            value=[
                {
                    "source_element": "EID",
                    "target_element": "EID",
                    "score": "0.807"
                },
                {
                    "source_element": "Cited by",
                    "target_element": "cited-by",
                    "score": "0.645"
                },
                {
                    "source_element": "zipcode",
                    "target_element": "postcode",
                    "score": "0.487"
                },
                {
                    "source_element": "Writers",
                    "target_element": "Schrijvers",
                    "score": "0.417"
                }
            ],
            response_only=True,  # the example only applies to response
        ),
        OpenApiExample(
            'Results with no matches',
            value=[[]],
            response_only=True,
        ),
    ]
)
class MatcherResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatcherResponse
        fields = ['source_element', 'target_element', 'score']
    source_element = serializers.CharField(required=True, max_length=100, allow_blank=True)
    target_element = serializers.CharField(required=True, max_length=100, allow_blank=True)
    score = serializers.DecimalField(max_digits=4, decimal_places=3)
