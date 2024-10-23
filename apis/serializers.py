#import serializer from Rest FW
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
#import Model 
from .models import Api


#from model create Serializers 

class Apiserializers(serializers.HyperlinkedModelSerializer):
    #specific Field from Model -> fields
    class Meta:
        model= Api
        fields = ('name','title','description') 