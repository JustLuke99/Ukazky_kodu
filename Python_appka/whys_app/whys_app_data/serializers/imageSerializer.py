from rest_framework import serializers
from whys_app_data.models.image import Image

class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    
    class Meta:
        model = Image
        fields = '__all__'