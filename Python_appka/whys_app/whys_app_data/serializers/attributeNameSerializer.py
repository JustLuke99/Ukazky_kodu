from rest_framework import serializers
from whys_app_data.models.attributeName import AttributeName

class AttributeNameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = AttributeName
        fields = '__all__'
