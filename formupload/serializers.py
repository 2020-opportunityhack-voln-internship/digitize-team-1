from rest_framework import serializers
from .models import Form

#Form serializer
class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = '__all__'
