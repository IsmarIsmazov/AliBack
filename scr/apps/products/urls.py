from django.urls import path

from .views import product_list_api_view, product_detail_api_view, category_list_api_view, \
    new_products_api_view, product_cart_list_api_view

urlpatterns = [
    path('products/categories/', category_list_api_view),
    path('products/products/', product_list_api_view),
    path('products/products/<int:id>/', product_detail_api_view),
    path('products/new-products/', new_products_api_view),
    path('products/product_cart/', product_cart_list_api_view),
]

