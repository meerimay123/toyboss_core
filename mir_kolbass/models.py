from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator
from django.db import models
from solo.models import SingletonModel


class Publication(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='publication/', verbose_name='Изображение')
    created_date = models.DateField(verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='product/', verbose_name='Изображение')
    description = models.TextField(verbose_name='описание')
    composition = models.CharField(max_length=100, verbose_name='состав')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукции'


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='recipe/', verbose_name='Изображение')
    composition = models.CharField(max_length=200, verbose_name='состав')
    product = models.ManyToManyField(
        Product,
        related_name='recipes',
        verbose_name='Продукты'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class SocialMediaContact(SingletonModel):
    phone_number = models.CharField(max_length=15, validators=[MinLengthValidator(7)], verbose_name='Номер телефона')
    facebook_list = models.URLField(blank=True, verbose_name='Ссылка на Facebook')
    instagram_list = models.URLField(blank=True, verbose_name='Ссылка на Instagram')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class About(models.Model):
    description = RichTextField(verbose_name='Описание')
    image = models.ImageField(upload_to='about/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
