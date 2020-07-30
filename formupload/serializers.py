from rest_framework import serializers
from .models import PaperForm


class PaperFormSerializer(serializers.ModelSerializer):
    """
    Serializer that converts the paper form model into JSON
    """
    class Meta:
        model = PaperForm
        fields = '__all__'