from django.contrib import admin
from .models import category
from .models import product

# Register your models here.
class display(admin.ModelAdmin):
    list_display = ['categoryname']

class productdisplay(admin.ModelAdmin):
    list = ('categoryname','product_name','price','quantity','description')
admin.site.register(category, display)
admin.site.register(product,productdisplay)