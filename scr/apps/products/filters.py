from django_filters import FilterSet, NumberFilter
from django_filters import rest_framework as filters
from .models import Product, Category


class ProductFilter(FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ('title', 'is_active', 'in_stock', 'category', 'slug')


class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = ('name', 'slug')
