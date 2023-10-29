from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_product_count(self, obj):
        return obj.product.count()
