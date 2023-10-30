from django.urls import path

from .views import product_list_api_view, product_detail_api_view, category_list_api_view, \
    new_products_api_view, product_cart_list_api_view, product_cart_detail_view

urlpatterns = [
    path('categories/', category_list_api_view),
    path('', product_list_api_view),
    path('<int:id>/', product_detail_api_view),
    path('new-products/', new_products_api_view),
    path('product_cart/', product_cart_list_api_view),
    path('product_cart/<int:id>/', product_cart_detail_view)

]
