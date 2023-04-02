from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from whys_app_data.models.attributeName import AttributeName
from whys_app_data.models.attributeValue import AttributeValue
from whys_app_data.models.attribute import Attribute
from whys_app_data.models.catalog import Catalog
from whys_app_data.models.image import Image
from whys_app_data.models.product import Product
from whys_app_data.models.productAttributes import ProductAttributes
from whys_app_data.models.productImage import ProductImage

from whys_app_data.serializers.attributeNameSerializer import AttributeNameSerializer
from whys_app_data.serializers.attributeValueSerializer import AttributeValueSerializer
from whys_app_data.serializers.attributeSerializer import AttributeSerializer
from whys_app_data.serializers.catalogSerializer import CatalogSerializer
from whys_app_data.serializers.imageSerializer import ImageSerializer
from whys_app_data.serializers.productAttributesSerializer import ProductAttributesSerializer
from whys_app_data.serializers.productImageSerializer import ProductImageSerializer
from whys_app_data.serializers.productSerializer import ProductSerializer

class ImportView(APIView):    
    """
    Zjištění, zda model s konkrétním ID již existuje
    @return None    Pokud model neexistuje
    @return model   Pokud model existuje
    """
    def get_existing_model_or_none(self, model, id):
        if model.objects.filter(id=id).exists():
            return model.objects.get(id=id)
        else:
            return None
    
    """
    Zjištění, zda model s konkrétním ID již existuje
    @param my_serializer    Serializer, který se použije pro vytvoření/aktualizaci záznamu
    @param model            Model, který se bude vytvářet/aktualizovat
    @param data             Data, která se vloží do záznamu
    """
    def create_or_update(self, my_serializer, model, data):
        model = self.get_existing_model_or_none(model, data["id"])
        
        if model != None:
            serializer = my_serializer(model, data)
        else:
            serializer = my_serializer(data=data) 
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            return Response(data="Data nelze uložit", status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request):
        if not isinstance(request.data, list):
            return Response(data="Spatny typ dat, musi se jednat o list", status=status.HTTP_400_BAD_REQUEST)
        
        for record in request.data:
            
            if len(list(record.keys())) != 1:
                return Response(data="Chyba v datech", status=status.HTTP_400_BAD_REQUEST)
            
            key, values = list(record.keys())[0], list(record.values())[0]
            
            if not isinstance(values, dict):
                return Response(data="Spatny typ dat pod nazvem modelu, musi se jednat o dict", status=status.HTTP_400_BAD_REQUEST)
            
            if not isinstance(values["id"], int):
                return Response(data="Spatny typ id", status=status.HTTP_400_BAD_REQUEST)
            
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
                case _:
                    return Response(data="Nazev modelu neexistuje", status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_201_CREATED)