
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from apps.produto.models import Produto


class ProdutoListView(ListView):
    model = Produto


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = '__all__'


class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy("list_produto")


class ProdutoCreateView(CreateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('list_produto')


class ProdutoDadosUpdateView(UpdateView):
    model = Produto
    fields = '__all__'


class ProdutoDetailView(DetailView):
    model = Produto
