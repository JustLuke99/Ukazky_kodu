from django import forms
from whys_app_data.models.attributeName import AttributeName
from whys_app_data.models.attributeValue import *
from whys_app_data.models.attribute import *
from whys_app_data.models.catalog import *
from whys_app_data.models.image import *
from whys_app_data.models.product import *
from whys_app_data.models.productAttributes import *
from whys_app_data.models.productImage import * 

class AttributeNameForm(forms.ModelForm):
    class Meta:
        model = AttributeName
        fields = ['nazev', 'kod', 'zobrazit']

class AttributeValueForm(forms.ModelForm):
    class Meta:
        model = AttributeValue
        fields = ['hodnota']

class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ['nazev_atributu_id', 'hodnota_atributu_id']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['nazev', 'description', 'cena', 'mena', 'published_on', 'is_published']

class ProductAttributesForm(forms.ModelForm):
    class Meta:
        model = ProductAttributes
        fields = ['attribute', 'product']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['nazev', 'obrazek']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['nazev', 'product', 'obrazek_id']

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ['products_ids']