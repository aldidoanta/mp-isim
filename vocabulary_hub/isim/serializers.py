from rest_framework import serializers
from isim.models import Isim, PricingInfo, MATCHERS


class PricingInfoSerializer(serializers.Serializer):
    class Meta:
        model = PricingInfo
        fields = ['intervals', 'price_per_interval']
    intervals = serializers.IntegerField(required=True, min_value=1)
    price_per_interval = serializers.IntegerField(required=True, min_value=1)

class IsimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isim
        fields = ['id', 'source_schema', 'target_schema', 'matcher', 'pricing_info']
    id = serializers.IntegerField(read_only=True)
    source_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)
    target_schema = serializers.CharField(required=True, allow_blank=True, max_length=100)
    matcher = serializers.ChoiceField(choices=MATCHERS, default=MATCHERS[0])
    pricing_info = PricingInfoSerializer(required=False)
