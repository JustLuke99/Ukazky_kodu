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

class ModelListView(APIView):
    def remove_null_values(self, obj):
        if isinstance(obj, list):
            return [self.remove_null_values(i) for i in obj if i is not None]
        elif isinstance(obj, dict):
            return {k: self.remove_null_values(v) for k, v in obj.items() if v is not None}
        else:
            return obj
    
    def get(self, request, nazev_modulu):
        match nazev_modulu:
                case "AttributeName":
                    data = AttributeName.objects.all()
                case "AttributeValue":
                    data = AttributeValue.objects.all()
                case "Image":
                    data = Image.objects.all()
                case "Product":
                    data = Product.objects.all()
                case "ProductAttributes": 
                    data = ProductAttributes.objects.all()
                case "Attribute": 
                    data = Attribute.objects.all()
                case "ProductImage":
                    data = ProductImage.objects.all()
                case "Catalog":
                    data = Catalog.objects.all()
                case other:
                    return Response(data="Nazev modelu neexistuje", status=status.HTTP_404_NOT_FOUND)

        json_data = json.loads(serializers.serialize("json", data))
        
        send_data = []
        for record in json_data:
            tmp_data = {}
            tmp_data[nazev_modulu] = {}
            
            tmp_data[nazev_modulu] = record["fields"]
            tmp_data[nazev_modulu]["id"] = record["pk"]
            
            tmp_data = self.remove_null_values(tmp_data)
            
            send_data.append(tmp_data)
        
        return Response(data=send_data, status=status.HTTP_200_OK)