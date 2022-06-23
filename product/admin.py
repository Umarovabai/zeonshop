from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from solo.admin import SingletonModelAdmin

from product.models import Category, Product, ProductItemImage, Help, AboutUs, OurAdvantages, PublicOffer, News, \
    Slider, Footer, FloatingButton, Help_image, Contacts


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


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(PublicOffer)
class PublicOfferAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(FloatingButton)
class FloatingButtonAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'type', 'created')
    list_filter = ('type', 'created')


admin.site.register(Help)


@admin.register(Help_image)
class Help_imageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(OurAdvantages)
admin.site.register(News)
admin.site.register(Category)
