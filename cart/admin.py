from django.contrib import admin

from cart.models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price1', 'old_price', 'quantity', 'recolor']

admin.site.register(Cart)