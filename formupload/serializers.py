from rest_framework import serializers
from .models import PaperForm

# Upload Paperform
class PaperFormCreateSerializer(serializers.ModelSerializer):
    """
    Serializer that converts the paper form model into JSON
    """
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = PaperForm
        fields = '__all__'

# Edit and Delete Paperforms
class PaperFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaperForm
        fields = '__all__'