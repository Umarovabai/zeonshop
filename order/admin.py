from django.contrib import admin

from order.models import OrderItem, Order


class CartItemInline(admin.TabularInline):
    model = OrderItem
    max_num = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline,

    ]


admin.site.register(Order, OrderAdmin)