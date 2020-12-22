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


# cria um produto fictício
@pytest.fixture
def produto(db):
    return mommy.make(Produto)


# resposta com o usuário logado
@pytest.fixture
def resp(cliente_com_usuario_logado, produto):
    resp = cliente_com_usuario_logado.get(reverse('detail_produto', kwargs={'pk': produto.pk}))
    return resp


# testa os dados do produto com o usuário logado
def test_dados(resp, produto):
    assert_contains(resp, produto.nome)
    assert_contains(resp, produto.descricao)



# resposta sem o usuário logado
@pytest.fixture
def resp_sem_usuario(client, produto):
    resp = client.get(reverse('detail_produto', kwargs={'pk': produto.pk}))
    return resp


# teste sem o usuário logado
def teste_sem_usuario_logado(resp_sem_usuario):
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))  # redirecionamento ao login
