from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world!')
from .models import Pdf
from django.contrib.auth.models import User
from polls.serializers import Pdfserializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated , AllowAny

class UserList(generics.ListCreateAPIView):
    queryset = Pdf.objects.all()
    serializer_class = Pdfserializers
    permission_classes = [AllowAny]

class Userupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pdf.objects.all()
    serializer_class = Pdfserializers
    permission_classes = [AllowAny]



# class profileListapiview(ListAPIView):
#     queryset = profile.objects.all()
#     serializer_class = profileserializer
#     permission_classes = [IsAuthenticated]

#     def list(self, request):
#         query = profile.objects.all()
#         serializers = profileserializer(query , many=True)
#         return Response({"status":"ok","data": serializers.data},status=status.HTTP_200_OK)

