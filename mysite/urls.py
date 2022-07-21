# デプロイ後でもエラーメッセージを見れるようにする
from shop import views

handler500 = views.my_customized_server_error


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('shop.urls')),
    path('admin/', admin.site.urls),
]
