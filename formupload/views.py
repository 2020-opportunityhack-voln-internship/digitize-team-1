from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import FormSerializer
from .models import Form


class FormViewSet(viewsets.ModelViewSet):
    """
    Takes all the files that are uploaded as form objects (created in models.py) and then serializes the data
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer