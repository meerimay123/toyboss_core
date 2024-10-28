from django.contrib import admin
from solo.admin import SingletonModelAdmin

from mir_kolbass.models import Product, Recipe, Publication, About, Category, SocialMediaContact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


# @admin.register(SocialMediaContact)
# class SocialMediaContactAdmin(admin.ModelAdmin):
#     list_display = ['instagram_list', 'facebook_list', 'phone_number']

admin.site.register(SocialMediaContact, SingletonModelAdmin)