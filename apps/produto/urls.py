from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.produto.views import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, \
    ProdutoDetailView

urlpatterns = [
    path('listar/', login_required(ProdutoListView.as_view()), name='list_produto'),
    path('novo/', login_required(ProdutoCreateView.as_view()), name='create_produto'),
    path('editar/<int:pk>/', login_required(ProdutoUpdateView.as_view()), name='edit_produto'),
    path('deletar/<int:pk>/', login_required(ProdutoDeleteView.as_view()), name='delete_produto'),
    path('detalhes/<int:pk>/', login_required(ProdutoDetailView.as_view()), name='detail_produto'),
]
