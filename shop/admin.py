from django.contrib import admin
from .models import  Product, PostTag, Detail, Detail_tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_field = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product, ProductAdmin)

admin.site.register(PostTag)

class DetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'baroint1', 'baroint2', 'baroint3']
    list_editable = ['price', 'baroint1', 'baroint2', 'baroint3']

admin.site.register(Detail, DetailAdmin)

admin.site.register(Detail_tag)