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


def index(request):
    context = {

    }
    return render(request, 'index.html', context)

