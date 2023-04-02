from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from whys_app_data.models.attributeName import AttributeName
from whys_app_data.models.attributeValue import *
from whys_app_data.models.attribute import *
from whys_app_data.models.catalog import *
from whys_app_data.models.image import *
from whys_app_data.models.product import *
from whys_app_data.models.productAttributes import *
from whys_app_data.models.productImage import * 

from whys_app_data.serializers.attributeNameSerializer import *
from whys_app_data.serializers.attributeValueSerializer import *
from whys_app_data.serializers.attributeSerializer import *
from whys_app_data.serializers.catalogSerializer import *
from whys_app_data.serializers.imageSerializer import *
from whys_app_data.serializers.productAttributesSerializer import *
from whys_app_data.serializers.productImageSerializer import *
from whys_app_data.serializers.productSerializer import *

class ImportView(APIView):    
    def get_existing_model_or_none(self, model, id):
        if model.objects.filter(id=id).exists():
            return model.objects.get(id=id)
        else:
            return None
    
    def create_or_update(self, my_serializer, model, data):
        model = self.get_existing_model_or_none(model, data["id"])
        
        if model != None:
            serializer = my_serializer(model, data)
        else:
            serializer = my_serializer(data=data)
            
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(data="Data nelze uložit", status=status.HTTP_400_BAD_REQUEST)

        
    def post(self, request):
        for record in request.data:
            if len(list(record.keys())) > 1:
                return Response(data="Chyba v datech", status=status.HTTP_400_BAD_REQUEST)
            
            key, values = list(record.keys())[0], list(record.values())[0]
            
            match key:
                case "AttributeName":
                    self.create_or_update(AttributeNameSerializer, AttributeName, values)

                case "AttributeValue":
                    self.create_or_update(AttributeValueSerializer, AttributeValue, values)
                
                case "Image":
                    self.create_or_update(ImageSerializer, Image, values)
                
                case "Product":
                    self.create_or_update(ProductSerializer, Product, values)
                
                case "ProductAttributes": 
                    self.create_or_update(ProductAttributesSerializer, ProductAttributes, values)
                
                case "Attribute": 
                    self.create_or_update(AttributeSerializer, Attribute, values)
                
                case "ProductImage":
                    self.create_or_update(ProductImageSerializer, ProductImage, values)
                
                case "Catalog":
                    self.create_or_update(CatalogSerializer, Catalog, values)
                    
                case other:
                    return Response(data="Nazev modelu neexistuje", status=status.HTTP_404_NOT_FOUND)

                    
        return Response(status=status.HTTP_201_CREATED)