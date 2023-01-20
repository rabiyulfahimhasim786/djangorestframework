from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello world!')
from .models import Pdf, Outputtext
from django.contrib.auth.models import User
from polls.serializers import Pdfserializers, Outputtextserializers
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



def pdfurl(request):
    documents = Pdf.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in documents:
        rank = obj.link
        num  =  obj.description
        #print(rank)
    print(rank)
    print(num)
    ringo = Outputtext.objects.create(urllink=rank, urldes=num)
    ringo.save()
    #print(rank[8:-5])
    #print('/media/'+rank[8:-5]+'.pdf')
    #pdfkit.from_url(rank, './media/pdf/'+str(num)+'.pdf')
    #pdfkit.from_url(rank, './media/pdf/'+num+'.pdf')
    return HttpResponse("Hello, world!"+str(ringo.id))

#outpt create needs then only we need to user create api view 
#class OutputList(generics.ListCreateAPIView):
class OutputList(generics.ListAPIView):
    queryset = Outputtext.objects.all()
    serializer_class = Outputtextserializers
    permission_classes = [AllowAny]

class Outputupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outputtext.objects.all()
    serializer_class = Outputtextserializers
    permission_classes = [AllowAny]
# class profileListapiview(ListAPIView):
#     queryset = profile.objects.all()
#     serializer_class = profileserializer
#     permission_classes = [IsAuthenticated]

#     def list(self, request):
#         query = profile.objects.all()
#         serializers = profileserializer(query , many=True)
#         return Response({"status":"ok","data": serializers.data},status=status.HTTP_200_OK)

