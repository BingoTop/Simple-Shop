from django.shortcuts import render
from django.views.generic import ListView
from .models import Product
from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.views.generic import DetailView
from order.forms import RegisterForm as OrderForm
from django.utils.decorators import method_decorator
from user.decorators import login_required
from user.decorators import admin_required
from rest_framework import generics
from rest_framework import mixins
from .serializers import ProductSerializer

# Create your views here.
class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    model = Product
    template_name = 'register_product.html'
    context_object_name = 'product_list'

    form_class = RegisterForm
    success_url = '/product'

    def form_valid(self,form):
        product = Product(
            name= form.data.get('name'),
            price = form.data.get('price'),
            description = form.data.get("description"),
            stock = form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)

        


class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all() # 필터로 조건 지정도 가능
    context_object_name = 'product'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = OrderForm(self.request)
        return context

