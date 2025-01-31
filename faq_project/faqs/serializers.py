from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    # Define fields for serialized FAQ data
    question = serializers.CharField()
    answer = serializers.CharField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
