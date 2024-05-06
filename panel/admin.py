from django.contrib import admin
from .models import Customer, PurchaseOrder, ShippingDetail

# Register your models here.
admin.site.register(Customer)
admin.site.register(PurchaseOrder)
admin.site.register(ShippingDetail)