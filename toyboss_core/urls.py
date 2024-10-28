"""
URL configuration for toyboss_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include



from mir_kolbass.views import ProductView, RecipesView, HomeView, PublicationView, AboutView, PublicationDetailView, \
    ProductsDetailView, RecipeDetailView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('home/', HomeView.as_view(), name='home'),
    path('product/', ProductView.as_view(), name='product'),
    path('product-detail/<int:pk>/', ProductsDetailView.as_view(), name='product-detail-list'),
    path('publication/', PublicationView.as_view(), name='publication'),
    path('publication-detail/<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('recipes/', RecipesView.as_view(), name='recipes'),
    path('recipes-detail/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
