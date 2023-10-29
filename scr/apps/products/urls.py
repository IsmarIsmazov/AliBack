from django.urls import path
from .views import productsViewList, productDetail

urlpatterns = [
    path('', productsViewList),
    path('<int:pk>', productDetail)
]
