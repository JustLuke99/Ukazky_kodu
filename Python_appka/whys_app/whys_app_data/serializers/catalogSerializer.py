from rest_framework import serializers
from whys_app_data.models.image import Image
from whys_app_data.models.product import Product
from whys_app_data.models.attribute import Attribute
from whys_app_data.models.catalog import Catalog

class CatalogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    obrazek_id = serializers.PrimaryKeyRelatedField(allow_null=True, required=False,
        queryset=Image.objects.all(),
    )
    products_ids = serializers.PrimaryKeyRelatedField(many=True, required=False,
        queryset=Product.objects.all(),
    )
    attributes_ids = serializers.PrimaryKeyRelatedField(many=True, required=False,
        queryset=Attribute.objects.all(),
    )
 
    class Meta:
        model = Catalog
        fields = '__all__'
        depth = 1