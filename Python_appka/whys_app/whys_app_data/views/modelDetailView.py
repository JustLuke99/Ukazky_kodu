from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

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

class ModelDetailView(APIView):   
    def get(self, request, nazev_modulu, id):
        match nazev_modulu:
            case "AttributeName":
                send_data = AttributeNameSerializer(get_object_or_404(AttributeName, pk=id))
            case "AttributeValue":
                send_data = AttributeValueSerializer(get_object_or_404(AttributeValue, pk=id))
            case "Image":
                send_data = ImageSerializer(get_object_or_404(Image, pk=id))
            case "Product":
                send_data = ProductSerializer(get_object_or_404(Product, pk=id))
            case "ProductAttributes": 
                send_data = ProductAttributesSerializer(get_object_or_404(ProductAttributes, pk=id))
            case "Attribute": 
                send_data = AttributeSerializer(get_object_or_404(Attribute, pk=id))
            case "ProductImage":
                send_data = ProductImageSerializer(get_object_or_404(ProductImage, pk=id))
            case "Catalog":
                send_data = CatalogSerializer(get_object_or_404(Catalog, pk=id))
            case _:
                return Response(data="Nazev modelu neexistuje", status=status.HTTP_404_NOT_FOUND)
        
        return Response(data=send_data.data, status=status.HTTP_200_OK)
