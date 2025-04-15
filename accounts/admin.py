from django.contrib import admin
from .models import Category, Product, Address, OrderItem, Order, OrderDetails, Checkout

# Register the Category model
admin.site.register(Category)

# Register the Product model
admin.site.register(Product)

admin.site.register(Address)

admin.site.register(OrderItem)

# admin.site.register(Order)

admin.site.register(OrderDetails)

admin.site.register(Checkout)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_amount', 'status') 

class buttonAdmin(admin.ModelAdmin ):
    change_form_template= "button.html "
