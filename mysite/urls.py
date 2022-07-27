# デプロイ後でもエラーメッセージを見れるようにする
# from shop import views

# handler500 = views.my_customized_server_error


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    path('cart/', include('cart.urls')),
    path('', include('shop.urls')),
]