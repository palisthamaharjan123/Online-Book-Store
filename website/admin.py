from django.contrib import admin

from .models import RequestBook

# Register your models here.
from .models import Book, Order
from .models import Author,Cart,Cartitems

admin.site.register(Book)
# admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Author)
admin.site.register(RequestBook)
admin.site.register(Cart)
admin.site.register(Cartitems)
# admin.site.register(ShippingAddress)
