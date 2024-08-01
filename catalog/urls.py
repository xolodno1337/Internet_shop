from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ContactTemplateView, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="product_list"),
    path("create", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path('category/', CategoryListView.as_view(), name='category_list'),
]
