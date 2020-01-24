from rest_framework import serializers

from curr_api.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'id',
            'code',
            'rate',
            'created_at',
            'modified_at'
        ]


class ExchangeRateSerializer(serializers.Serializer):
    from_curr = serializers.CharField(
        max_length=4,
        allow_blank=False
    )
    to_curr = serializers.CharField(
        max_length=4,
        allow_blank=False
    )
    from_amount = serializers.FloatField(
        allow_null=False
    )

    class Meta:
        fields = [
            'from_curr',
            'to_curr',
            'from_amount',
        ]

    def validate_from_curr(self, value):
        try:
            Currency.objects.get(code=value)
        except Currency.DoesNotExist:
            raise serializers.ValidationError("Currency does not exist")
        return value

    def validate_to_curr(self, value):
        try:
            Currency.objects.get(code=value)
        except Currency.DoesNotExist:
            raise serializers.ValidationError("Currency does not exist")
        return value
