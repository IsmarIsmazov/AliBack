from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.utils import timezone

from .models import Product, Category, ProductCart
from .permissions import IsOwnerOrReadOnly
from .serializers import ProductListSerializer, CategorySerializer, ProductCartSerializer, ProductDetailSerializer
from .filters import ProductFilter, CategoryFilter


@api_view(['GET'])
def new_products_api_view(request):
    midnight = timezone.localtime().replace(hour=0, minute=0, second=0, microsecond=0)
    new_products = Product.objects.filter(created__gte=midnight).order_by('created')
    serializer = ProductListSerializer(new_products, context={"request": request}, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_list_api_view(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        product_filters = ProductFilter(request.GET, queryset=queryset)
        filtered_product = product_filters.qs
        sort_by_price = request.query_params.get('price', None)

        if sort_by_price == 'min':
            filtered_product = filtered_product.order_by('price')
        elif sort_by_price == 'max':
            filtered_product = filtered_product.order_by('-price')
        serializer = ProductListSerializer(filtered_product, context={"request": request}, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrReadOnly])
def product_detail_api_view(request, id):
    try:
        queryset = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductDetailSerializer(queryset)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ProductDetailSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        queryset.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def category_list_api_view(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_cart_list_api_view(request):
    if request.method == 'GET':
        queryset = ProductCart.objects.filter(user=request.user)
        serializer = ProductCartSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrReadOnly])
def product_cart_detail_view(request, id):
    try:
        queryset = ProductCart.objects.get(id=id, user=request.user)
    except ProductCart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductCartSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductCartSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
