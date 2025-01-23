from django.contrib import admin
from backend.models import (
                    User,
                    Shop,
                    Category,
                    Product,
                    ProductInfo,
                    Parameter,
                    ProductParameter,
                    Contact,
                    Order,
                    OrderItem)


admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInfo)
admin.site.register(Parameter)
admin.site.register(ProductParameter)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderItem)

