import pytest
from django.urls import reverse
from model_mommy import mommy

from gs_project.django_assertions import assert_contains


@pytest.fixture
def usuario_logado(db, django_user_model):
    usuario_model = mommy.make(django_user_model, first_name='fulano')
    return usuario_model


@pytest.fixture
def cliente_com_usuario_logado(usuario_logado, client):
    client.force_login(usuario_logado)
    return client


@pytest.fixture
def resp(cliente_com_usuario_logado):
    resp = cliente_com_usuario_logado.get(reverse('base:home'))
    return resp


# testa se pagna da home existe
def test_status_code(resp):
    assert resp.status_code == 200


# testa titulo
def test_title(resp):
    assert_contains(resp, '<title>Home</title>')


# testa link para a pag home
def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}"')


# testa link para a lista de clientes
def test_lista_clientes_link(resp):
    assert_contains(resp, f'href="{reverse("list_produto")}"')


# testa link para o cadastro de clientes
def test_cadastro_clientes_link(resp):
    assert_contains(resp, f'href="{reverse("create_produto")}"')


# testa link para o portifolio
def test_portifolio_link(resp):
    assert_contains(resp, 'href="https://ravellys.github.io"')
