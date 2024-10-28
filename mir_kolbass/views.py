from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Product, Publication, Recipe, Category, About, SocialMediaContact


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'about': About.objects.first(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = {
            'product-list': Product.objects.all(),
            'product_category': Category.objects.all(),
            'social_media': SocialMediaContact.objects.first()

        }
        return context


class RecipesView(TemplateView):
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        recipes = Recipe.objects.all()
        paginator = Paginator(recipes, 1)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'social_media': SocialMediaContact.objects.first()

        }
        return context


class PublicationView(TemplateView):
    template_name = 'publications.html'

    def get_context_data(self, **kwargs):
        publications = Publication.objects.all()
        paginator = Paginator(publications, 1)
        # try:
        #     page_number = self.request.GET['page']
        # except KeyError:
        #     page_number = 1
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'social_media': SocialMediaContact.objects.first()

        }
        return context


class AboutView(TemplateView):
    template_name = 'about-company.html'

    def get_context_data(self, **kwargs):
        context = {
            'about': About.objects.first(),
            'social_media': SocialMediaContact.objects.first()

        }
        return context


class PublicationDetailView(TemplateView):
    template_name = 'publications-inner.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        publication = get_object_or_404(Publication, id=publication_pk)
        context = {
            'publication': publication,
            'social_media': SocialMediaContact.objects.first()

        }
        return context


class ProductsDetailView(TemplateView):
    template_name = 'product-inner.html'

    def get_context_data(self, **kwargs):
        product_pk = kwargs['pk']
        product = get_object_or_404(Product, id=product_pk)
        recipes = Recipe.objects.filter(product=product)

        related_products = (Product.objects
                            .filter(category=product.category)
                            .exclude(id=product_pk))
        context = {
            'product': product,
            'recipes': recipes,
            'related_products': related_products,
            'social_media': SocialMediaContact.objects.first()

        }
        return context


class RecipeDetailView(TemplateView):
    template_name = 'recipes-inner.html'

    def get_context_data(self, **kwargs):
        recipe_pk = kwargs['pk']
        context = {
            'recipes-detail-list': Recipe.objects.get(id=recipe_pk),
            'social_media': SocialMediaContact.objects.first(),

        }
        return context


