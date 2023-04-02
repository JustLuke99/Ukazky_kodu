from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
import json

from whys_app_data.models.attributeName import AttributeName
from whys_app_data.models.attributeValue import *
from whys_app_data.models.attribute import *
from whys_app_data.models.catalog import *
from whys_app_data.models.image import *
from whys_app_data.models.product import *
from whys_app_data.models.productAttributes import *
from whys_app_data.models.productImage import * 

class ModelDetailView(APIView):
    def remove_null_values(self, obj):
        if isinstance(obj, list):
            return [self.remove_null_values(i) for i in obj if i is not None]
        elif isinstance(obj, dict):
            return {k: self.remove_null_values(v) for k, v in obj.items() if v is not None}
        else:
            return obj
    
    def get(self, request, nazev_modulu, id):
        match nazev_modulu:
                case "AttributeName":
                    data = AttributeName.objects.filter(id=id)
                case "AttributeValue":
                    data = AttributeValue.objects.filter(id=id)
                case "Image":
                    data = Image.objects.filter(id=id)
                case "Product":
                    data = Product.objects.filter(id=id)
                case "ProductAttributes": 
                    data = ProductAttributes.objects.filter(id=id)
                case "Attribute": 
                    data = Attribute.objects.filter(id=id)
                case "ProductImage":
                    data = ProductImage.objects.filter(id=id)
                case "Catalog":
                    data = Catalog.objects.filter(id=id)
                case other:
                    return Response(data="Nazev modelu neexistuje", status=status.HTTP_404_NOT_FOUND)
        
        if data:
            send_data = {}
            send_data[nazev_modulu] = {}
            
            json_data = json.loads(serializers.serialize("json", data))[0]
            send_data[nazev_modulu] = json_data["fields"]
            send_data[nazev_modulu]["id"] = json_data["pk"]
            
            send_data = self.remove_null_values(send_data)
        
            return Response(data=send_data, status=status.HTTP_200_OK)
        return Response(data="Model s takovým ID neexistuje", status=status.HTTP_404_NOT_FOUND)
        