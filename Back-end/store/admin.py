from django.contrib import admin
from store.models import Product,Category, Gallery, Specification, Color, Size, Cart, CartOrder, CartOrderItem, Wishlist, Coupon, Notification, Review, ProductFaq

class GalleryInLine(admin.TabularInline):
    model = Gallery
    extra = 0

class SpecficationInLine(admin.TabularInline):
    model = Specification
    extra =0

class ColorInLine(admin.TabularInline):
    model = Color
    extra = 0

class SizeInLine(admin.TabularInline):
    model = Size
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'shipping_amount', 'stock_qty', 'in_stock','vendor', 'featured']
    list_filter = ['date'] 
    list_editable = ['featured'] 
    search_fields = ['title']
    inlines =[GalleryInLine, SpecficationInLine,ColorInLine,SizeInLine ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartOrder)
admin.site.register(CartOrderItem)
admin.site.register(Review)
admin.site.register(ProductFaq)
admin.site.register(Notification)
admin.site.register(Coupon)
admin.site.register(Wishlist)