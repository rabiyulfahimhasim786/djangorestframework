from rest_framework import serializers
from .models import Pdf

class Pdfserializers(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = '__all__'