from django.contrib import admin
from django.utils import timezone
from .models import *

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Productview)
admin.site.register(ProductColor)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Otracker)
admin.site.register(Orderitem)
admin.site.register(ReturnRequest)
admin.site.register(PickupAgent)
admin.site.register(Compare)
admin.site.register(Wishlist)
admin.site.register(FlashSale)
admin.site.register(Coupon)
admin.site.register(CouponUsage)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print("SAVE MODEL CALLED")
        if obj.orderstatus == "Processing" and obj.processing_at is None:
            obj.processing_at = timezone.now()
        elif obj.orderstatus == "Shipped" and obj.shipped_at is None:
            obj.shipped_at = timezone.now()
        elif obj.orderstatus == "Delivered" and obj.delivered_at is None:
            obj.delivered_at = timezone.now()
        super().save_model(request, obj, form, change)

