from rest_framework import serializers
from isim.models import Isim, MATCHERS


class IsimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isim
        fields = ['id', 'dataprovider_schema', 'dataconsumer_schema', 'matcher']
    id = serializers.IntegerField(read_only=True)
    dataprovider_schema = serializers.CharField(required=False, allow_blank=True, max_length=100)
    dataconsumer_schema = serializers.CharField(required=False, allow_blank=True, max_length=100)
    matcher = serializers.ChoiceField(choices=MATCHERS, default=MATCHERS[0])
