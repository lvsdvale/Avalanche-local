from .models import *
def post_save_itemcarrinho(instance,**kwargs):
    if instance.quantidade < 1:
        instance.delete()
models.signals.post_save.connect(post_save_itemcarrinho,sender=itemcarrinho,dispatch_uid='post_save_itemcarrinho')
