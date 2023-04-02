from django.contrib import admin
from whys_app_data.models.attributeName import AttributeName
from whys_app_data.models.attributeValue import AttributeValue
from whys_app_data.models.attribute import Attribute
from whys_app_data.models.catalog import Catalog
from whys_app_data.models.image import Image
from whys_app_data.models.product import Product
from whys_app_data.models.productAttributes import ProductAttributes
from whys_app_data.models.productImage import ProductImage

admin.site.register(AttributeName)
admin.site.register(AttributeValue)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(Image)
admin.site.register(ProductImage)
admin.site.register(Catalog)
