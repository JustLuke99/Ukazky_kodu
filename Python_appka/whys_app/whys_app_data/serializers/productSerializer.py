from rest_framework import serializers
from whys_app_data.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = Product
        fields = '__all__'
