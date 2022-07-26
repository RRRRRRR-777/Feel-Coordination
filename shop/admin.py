from django.contrib import admin
from .models import  Product, PostTag, Detail, Detail_tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock']
    list_editable = ['price', 'stock']
    prepopulated_field = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product, ProductAdmin)

admin.site.register(PostTag)

class DetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'baroint1', 'baroint2', 'baroint3']
    list_editable = ['price', 'slug', 'baroint1', 'baroint2', 'baroint3']

admin.site.register(Detail, DetailAdmin)

admin.site.register(Detail_tag)