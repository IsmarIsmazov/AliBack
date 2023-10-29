from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, context={"request": request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        queryset = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = ProductSerializer(request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProductSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, context={"request": request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        queryset = CategorySerializer.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer = CategorySerializer(request.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CategorySerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)