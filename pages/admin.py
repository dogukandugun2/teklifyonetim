from django.contrib import admin
from .models import Company,Product,OfferProduct,Offer
# Register your models here.
@admin.register(Company)
class AppAdmin(admin.ModelAdmin):
    list_display = ("name","slug",)
    readonly_fields = ("slug",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("description","size","quality","color","paint","zinc")



admin.site.register(Offer)
admin.site.register(OfferProduct)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('company', 'offer_type', 'created_at', 'total_value')