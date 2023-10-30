from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product',
                                 verbose_name='Категория')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator',
                             verbose_name='Создано пользователем')
    title = models.CharField(max_length=255, verbose_name='Название продукта')
    author = models.CharField(max_length=255, default='admin', verbose_name='Автор')
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    is_active = models.BooleanField(default=True, verbose_name='Доступность')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-created',)

    def __str__(self):
        return self.title


class ProductCart(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
