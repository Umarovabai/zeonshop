from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from product.models import Category, Product, ProductItemImage, Help, About_us, OurAdvantages, PublicOffer, News, \
    Slider, Footer, FloatingButton


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductItemImageAdmin(admin.StackedInline):
    model = ProductItemImage
    max_num = 8


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [
        ProductItemImageAdmin,

    ]


@admin.register(About_us)
class ProductAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >=1:
            return False
        return super().has_add_permission(request)


@admin.register(PublicOffer)
class ProductAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Slider)
class ProductAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Footer)
class ProductAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(FloatingButton)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'type', 'created')
    list_filter = ('type', 'created')


admin.site.register(Category)
admin.site.register(Help)
admin.site.register(OurAdvantages)
admin.site.register(News)
