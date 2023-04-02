from django import forms
from whys_app_data.models.attributeName import AttributeName
from whys_app_data.models.attributeValue import AttributeValue
from whys_app_data.models.attribute import Attribute
from whys_app_data.models.catalog import Catalog
from whys_app_data.models.image import Image
from whys_app_data.models.product import Product
from whys_app_data.models.productAttributes import ProductAttributes
from whys_app_data.models.productImage import ProductImage

class AttributeNameForm(forms.ModelForm):
    class Meta:
        model = AttributeName
        fields = '__all__'

class AttributeValueForm(forms.ModelForm):
    class Meta:
        model = AttributeValue
        fields = '__all__'

class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductAttributesForm(forms.ModelForm):
    class Meta:
        model = ProductAttributes
        fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = '__all__'

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = '__all__'
