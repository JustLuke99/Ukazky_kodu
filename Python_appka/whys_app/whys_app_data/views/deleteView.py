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

class DeleteAll(APIView):
    def get(self, request):
        AttributeName.objects.all().delete()
        AttributeValue.objects.all().delete()
        Attribute.objects.all().delete()
        Product.objects.all().delete()
        ProductAttributes.objects.all().delete()
        Image.objects.all().delete()
        ProductImage.objects.all().delete()
        Catalog.objects.all().delete()
        
        return Response(status=status.HTTP_200_OK)
