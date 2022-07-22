from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [path('', views.all_products, name='all_product'),
               path('<slug:detail_slug>', views.Detail_detail, name='product_detail'),
]