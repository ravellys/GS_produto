from rest_framework import serializers
from apps.produto.models import Produto


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Produto
        fields = ('pk', 'nome', 'descricao', 'valor')
