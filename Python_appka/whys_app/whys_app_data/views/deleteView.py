from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from whys_app_data.models import *
from whys_app_data.models.attributeName import *
from whys_app_data.models.attributeValue import *
from whys_app_data.models.attribute import *
from whys_app_data.models.product import *
from whys_app_data.models.productAttributes import *
from whys_app_data.models.image import *
from whys_app_data.models.productImage import *
from whys_app_data.models.catalog import *

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
        
        return Response(status=status.HTTP_205_RESET_CONTENT)
