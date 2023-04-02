from rest_framework import serializers
from whys_app_data.models.product import Product
from whys_app_data.models.image import Image
from whys_app_data.models.productImage import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
    )
    obrazek_id = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(),
    )

    class Meta:
        model = ProductImage
        fields = '__all__'
