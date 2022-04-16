import base64

from .models import TimestampRequest
from .serializers import TimestampSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Timestamp(APIView):

    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        timestamp_req = TimestampRequest.objects.all()
        serializer = TimestampSerializer(timestamp_req, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TimestampSerializer(data=request.data)
        if serializer.is_valid():
            pdf_file = request.data['pdf_file']
            b64_data =pdf_file.split(',')[1]
            
            data=base64.b64decode(b64_data.encode())

            with open(r'C:\Users\daisu\Downloads\test.pdf', 'wb') as f:
                f.write(data)  # バイナリファイルにはバイト列しか渡せない

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

