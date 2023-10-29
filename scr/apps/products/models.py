from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/categories')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    discription = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    image = models.ImageField(upload_to='media/products', verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    data_add = models.DateField(auto_now_add=True, verbose_name="Дата добавления")
    data_update = models.DateField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
