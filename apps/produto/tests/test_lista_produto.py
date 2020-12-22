import pytest
from django.urls import reverse
from model_mommy import mommy

from gs_project.django_assertions import assert_contains
from apps.produto.models import Produto


# criado para testes com o usuário logado
@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_model = mommy.make(django_user_model, first_name='fulano')
    return usuario_model


@pytest.fixture
def cliente_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client


# cria três produtos fictícios
@pytest.fixture
def produto(db):
    return mommy.make(Produto, 3)


# resposta com o usuário logado
@pytest.fixture
def resp(cliente_com_usuario_logado, produto):
    return cliente_com_usuario_logado.get(reverse('list_produto'))


# testa se pagna da lista de produtos existe
def test_lista_disponivel(resp):
    assert resp.status_code == 200


# verifica os dados dos produtos
def test_dados(resp, produto):
    for p in produto:
        assert_contains(resp, p.nome)
        assert_contains(resp, p.descricao)


# verifica link para alterar produto
def test_link_alterar(resp, produto):
    for p in produto:
        assert_contains(resp, reverse('edit_produto', kwargs={'pk': p.pk}))


# verifica link para deletar produto
def test_link_deletar(resp, produto):
    for p in produto:
        assert_contains(resp, reverse('delete_produto', kwargs={'pk': p.pk}))


# verifica link para cadastrar produto
def test_link_cadastrar(resp, produto):
    assert_contains(resp, reverse('create_produto'))
