from rest_framework import serializers


class ErrorMessageSerializer(serializers.Serializer):
    display_text = serializers.CharField(required=True)
    error_code = serializers.IntegerField(required=True)
