from rest_framework import serializers
from whys_app_data.models.attributeName import AttributeName
from whys_app_data.models.attributeValue import AttributeValue
from whys_app_data.models.attribute import Attribute

class AttributeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    nazev_atributu_id = serializers.PrimaryKeyRelatedField(
        queryset=AttributeName.objects.all(),
    )
    hodnota_atributu_id = serializers.PrimaryKeyRelatedField(
        queryset=AttributeValue.objects.all(),
    )

    class Meta:
        model = Attribute
        fields = '__all__'
