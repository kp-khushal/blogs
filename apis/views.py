from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
#local data import
from .serializers import Apiserializers
from .models import Api



#create class fro virewset
class Apiviewset(viewsets.ModelViewSet):
    #define quertset 
    queryset = Api.objects.all()
    #serializers class call
    serializer_class = Apiserializers