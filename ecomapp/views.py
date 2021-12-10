from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import *

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list']  = Product.objects.all().order_by('-id')
        context['allcategories'] = Category.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "about.html"

class CantactView(TemplateView):
    template_name = "contactus.html"   


class AllProductsView(TemplateView):
    template_name = "allproducts.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = Category.objects.all()
        return context


class ProductsDetailView(TemplateView):
    template_name = "productdeatil.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        product.view_count += 1
        product.save()
        context['product'] = product
        context['allcategories'] = Category.objects.all()
        return context

class AddToCartView(TemplateView):
    template_name = 'addtocart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['pro_id']
        product_obj = Product.objects.get(id=product_id)
        cart_id = self.request.session("cart_id",None)
        print(product_obj)
        return context


class CategoryDetailView(TemplateView):
    template_name = 'categorydeatil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoryID = self.kwargs['cat_id']
        products = None
        products = Product.get_all_products_by_categoryid(categoryID)
        context['allcategories'] = Category.objects.all()
        context['products'] = products
        return context