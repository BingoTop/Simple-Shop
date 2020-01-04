"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from user.views import index
from user.views import RegisterView
from user.views import LoginView
from product.views import ProductList
from product.views import ProductCreate
from product.views import ProductDetail
from order.views import OrderCreate
from order.views import OrderList
from user.views import logout
from product.views import ProductListAPI
from product.views import ProductDetailAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',logout),
    path('product/',ProductList.as_view(),name='product_list'),
    path('product/create/',ProductCreate.as_view(),name='product_create'),
    path('product/<int:pk>/',ProductDetail.as_view(),name='product_detail'),
    path('order/create/',OrderCreate.as_view(),name='oreder_create'),
    path('order/',OrderList.as_view(),name='oreder_list'),
    path('api/product/',ProductListAPI.as_view()),
    path('api/product/<int:pk>',ProductDetailAPI.as_view()),
]
