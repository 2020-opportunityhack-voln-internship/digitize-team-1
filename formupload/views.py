from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import FormSerializer
from .models import Form

# Create your views here.
class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer