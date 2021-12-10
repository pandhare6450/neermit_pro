from django.urls import path
from .views import *



app_name = "ecomapp"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", CantactView.as_view(), name="contact"),
    path("all-products/", AllProductsView.as_view(),name="allproducts"),
    path("products/<slug:slug>/", ProductsDetailView.as_view(),name="productdetail"),
    path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(),name="addtocart"),
    path("category-<slug:cat_id>/",CategoryDetailView.as_view(),name="categorydeatil"),
    

    
]
