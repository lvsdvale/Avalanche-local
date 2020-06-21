from .models import itemcarrinho
def itemcarrinhomiddleware(get_response):
    def middleware(request):

        chave = request.session.session_key
        response = get_response(request)
        if request.session.session_key is not None:
            if chave is not request.session.session_key:
                itemcarrinho.objects.filter(chave=chave).update(chave = request.session.session_key)
            if request.user.is_authenticated:
                if request.user.get_socio:
                    chave = request.session.session_key
                    itens = itemcarrinho.objects.filter(chave=chave)
                    for item in itens:
                        itemcarrinho.objects.filter(chave=chave).update(preco = item.produto.p_socio)
        return response
    return middleware