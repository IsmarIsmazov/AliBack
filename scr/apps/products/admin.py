from django.contrib import admin

from .models import Product, Category, ProductCart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'price', 'category',
        'in_stock', 'created', 'updated'
    )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created', 'updated')
    search_fields = ('title',)
    readonly_fields = ('created', 'updated')
    list_per_page = 20
    ordering = ('-created',)


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
