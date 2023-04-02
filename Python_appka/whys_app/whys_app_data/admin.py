from django.contrib import admin
from whys_app_data.models.attributeName import *
from whys_app_data.models.attributeValue import *
from whys_app_data.models.attribute import *
from whys_app_data.models.catalog import *
from whys_app_data.models.image import *
from whys_app_data.models.product import *
from whys_app_data.models.productAttributes import *
from whys_app_data.models.productImage import * 

admin.site.register(AttributeName)
admin.site.register(AttributeValue)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttributes)
admin.site.register(Image)
admin.site.register(ProductImage)
admin.site.register(Catalog)