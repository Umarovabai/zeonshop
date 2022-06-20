from django.contrib import admin

from basket.models import Cart, OrderItem, Order

admin.site.register(Cart)

class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'stock']


class OrderInline(admin.TabularInline):
    model = OrderItem
    max_num = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,

    ]


admin.site.register(Order, OrderAdmin)



