from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductListSerializer, CategorySerializer, ProductDetailSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def productsViewList(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductListSerializer(product,context={'request': request}, many=True).data
        return Response(data=serializer)
    elif request.method == 'POST':
        serializer = ProductDetailSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def productDetail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductDetailSerializer(request.data)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
