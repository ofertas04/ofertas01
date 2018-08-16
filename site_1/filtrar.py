from .models import Produto
import django_filters

class ProdutoFilter(django_filters.FilterSet):
    class Meta:
        model = Produto
        fields = ['codigo_acesso', ]