from django.contrib import admin

from .models import Product
# Register your models here.

# admin.site.register(Product)


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    list_filter = ('Qty', 'Price', 'Name')
    list_display = ('SKU', 'Name', 'Qty', 'Price')
