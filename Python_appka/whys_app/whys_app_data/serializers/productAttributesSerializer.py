from rest_framework import serializers
from whys_app_data.models.attribute import Attribute
from whys_app_data.models.product import Product
from whys_app_data.models.productAttributes import ProductAttributes

class ProductAttributesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    attribute = serializers.PrimaryKeyRelatedField(
        queryset=Attribute.objects.all(),
    )
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
    )

    class Meta:
        model = ProductAttributes
        fields = '__all__'
