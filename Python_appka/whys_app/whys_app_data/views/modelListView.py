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


class ModelListView(APIView):   
    def get(self, request, nazev_modulu):
        match nazev_modulu:
            case "AttributeName":
                data = AttributeNameSerializer(AttributeName.objects.all(), many=True)
            case "AttributeValue":
                data = AttributeValueSerializer(AttributeValue.objects.all(), many=True)
            case "Image":
                data = ImageSerializer(Image.objects.all(), many=True)
            case "Product":
                data = ProductSerializer(Product.objects.all(), many=True)
            case "ProductAttributes": 
                data = ProductAttributesSerializer(ProductAttributes.objects.all(), many=True)
            case "Attribute": 
                data = AttributeSerializer(Attribute.objects.all(), many=True)
            case "ProductImage":
                data = ProductImageSerializer(ProductImage.objects.all(), many=True)
            case "Catalog":
                data = CatalogSerializer(Catalog.objects.all(), many=True)
            case _:
                return Response(data="Nazev modelu neexistuje", status=status.HTTP_404_NOT_FOUND)

        return Response(data=data.data, status=status.HTTP_200_OK)
      
