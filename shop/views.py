import itertools

from django.http import Http404
from django.shortcuts import render

from shop_products.models import Product
from shop_products_category.models import ProductCategory
from shop_slider.models import Slider
from shop_settings.models import SiteSetting
from shop_products.views import ProductsListByCategory

def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting':site_setting

    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        "setting":site_setting
    }
    return render(request, 'shared/Footer.html', context)

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def home_page(request,*args,**kwargs):
    sliders = Slider.objects.all()
    most_visit_products = Product.objects.order_by('-visit_count').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]
    group_products = Product.objects.order_by('categories__product').distinct()[:8]
    categories = ProductCategory.objects.all()

    context = {
        'data': 'این سایت فروشگاهی با فریم ورک django نوشته شده',
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products),
        'group_products':my_grouper(4,group_products),
        'categories':categories,




    }
    return render(request, 'home_page.html', context)

def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        "setting": site_setting
    }
    return render(request,'about_page.html',context)

