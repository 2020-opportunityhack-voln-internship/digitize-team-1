from rest_framework import serializers
from .models import Form

#Form serializer that converts data into json that react will read
class FormSerializer(serializers.ModelSerializer):
    """
    Serializes data which converts django models to json format which react will read and vice versa
    """
    class Meta:
        model = Form
        fields = '__all__'
