from django.contrib import admin

from basket.models import Cart, Order, Orders

admin.site.register(Cart)


class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'stock']


admin.site.register(Order)
admin.site.register(Orders)



