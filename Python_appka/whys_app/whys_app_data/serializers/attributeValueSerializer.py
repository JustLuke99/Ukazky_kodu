from rest_framework import serializers
from whys_app_data.models.attributeValue import AttributeValue

class AttributeValueSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = AttributeValue
        fields = '__all__'