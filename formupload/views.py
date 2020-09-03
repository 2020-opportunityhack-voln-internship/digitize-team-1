
from .serializers import PaperFormSerializer
from .models import PaperForm
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


class PaperFormUploadView(APIView):

    """
    API View that handles uploading paper forms to the database
    """

    #parser to read raw file uploads
    parser_classes = (MultiPartParser, FormParser)

    """
    GET requests
    """
    def get(self, request, *args, **kwargs):
        paper_form = PaperForm.objects.all()
        serializer = PaperFormSerializer(paper_form, many=True)
        return Response(serializer.data)

    """
    POST requests
    """
    def post(self, request, *args, **kwargs):
        paper_form_serializer = PaperFormSerializer(data=request.data)
        if paper_form_serializer.is_valid():
            paper_form_serializer.save()
            return Response(paper_form_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', paper_form_serializer.errors)
            return Response(paper_form_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
