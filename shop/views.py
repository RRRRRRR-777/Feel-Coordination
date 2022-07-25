# デプロイ後でもエラーメッセージを見れるようにする
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError

@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)


from django.shortcuts import render

from shop.models import Product, Detail, PostTag

from django.core.paginator import Paginator, EmptyPage, InvalidPage

from django.db.models import Q



# import code
# console = code.InteractiveConsole(locals=locals()) # <- locals=locals() が重要
# console.interact()


def all_products(request):
    products_list = Product.valid_objects.all()
    details = Detail.objects.all()
    posts = PostTag.objects.all()

    paginator = Paginator(products_list, per_page=12)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    data = {'products': products,
            'details': details,
            'posts': posts,
            'apple': 'りんご',
    }

    return render(request, 'product_list.html', data)

# 新しい商品detailのやつ
def Detail_detail(request, detail_slug):
    try:
        product = Detail.objects.get(slug=detail_slug)
    except Exception as e:
        raise e

    products = Product.objects.all()

    query = None
    detail = None

    if 'd' in request.GET:
        query = request.GET.get('d')
        detail = Detail.objects.all().order_by('price').filter(Q(subtag__name__contains=query))


    data = {'product': product,
            'apple': 'りんご',
            'detail': detail,
            'query': query,
            'products': products,
    }

    return render(request, 'product_detail.html', data)
