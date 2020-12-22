# GS_produto
📜 Este repositório trata-se de um projeto para realizar o CRUD (Create, Read, Update, Delete) de uma entidade Produto com o framework Django. Utilizou-se o método da Class Based Views (CBV) para automatizar e facilitar o encapsulamento das funcionalidades. Para a realização dos testes foi utilizado o pytest-django e como ambiente virtual utilizou-se o pipenv. Foi desenvolvida uma infraestrutura para o banco de dados postgrs, com as ferramentas Docker e Docker Compose. Utilizou-se o Django Rest Framework (DRF) para servir APIs. Por fim utilizou-se o framework frontend ReactJS para consumir a API do DRF.
O projeto ainda foi posto em produção no heroku - link do deploy: [GS_produto](https://gsproduto.herokuapp.com/).

 
## 💻 Configuração para Desenvolvimento

### Programas necessários
Aqui está a lista de coisas que você precisa configurar em sua máquina para utilizar este repositório:

1. Python 3  (se você estiver usando Linux, é provável que já esteja instalado. Execute o comando python3 -V para verificar)
2. Pip  (o instalador de pacote Python padrão)
3. NodeJS (em uma versão 6 ou superior) e npm  (5.2+)
4. Docker e Docker Compose


### Aplicação Django

1. Inicialmente insira como variaveis globais no sistema:
```
PIPENV_VENV_IN_PROJECT=1
PIPENV_IGNORE_VIRTUALENVS=1
```

2. Instale o pipenv
```
pip install pipenv
```

3. Instale as dependências de desenvolvimento
```
pipenv sync -d
```

4. Execute o comando do Docker Compose.

```
docker-compose up
```

5. Crie um arquivo _.env_ com as configurações presentes em _contrib/env-sample_

```
DEBUG=TRUE
SECRET_KEY=defina sua chave secreta
ALLOWED_HOSTS=localhost, 127.0.0.1
DATABASE_URL=postgres://{{usuário do docker}}:{{senha do docker}}@localhost:{{porta}}/{{banco de dados}}
```


6. Verifique a formatação do código segundo a PEP8 com o flake8 
```
pipenv run flake8 .
```

7. Execute os testes 
```
pipenv run pytest
```

8. Ative o shell do pipenv no seu prompt de comando:
```
pipenv shel
```

9. Execute o projeto:
```
python manage.py runserver
```

10. realize as migrações para se banco de dados:
```
python manage.py makemigrations
python manage.py migrate
```

11. Para criar o super usuário no se banco de dado utilize:
```
python manage.py createsuper user
```

12. Para executar a aplicação utilize:
```
python manage.py runserver
```

![Site demonstração](https://github.com/ravellys/GS_produto/blob/main/arquivos/django_template.gif)


### API - Django Rest Framework:
A API construida com o DRF pode ser obtida apartir do enpoint `ttp://localhost:8000/api/produto/`.
![DRF demonstralção](https://github.com/ravellys/GS_produto/blob/main/arquivos/DRF.gif)


### Consulta da API com  ReactJS:
A consulta da API com o framework ReactJA pode ser observada na pasta gs_frontend.
para executa-la você pode utilizar o comando 
```
npm start
```
![React Demonstração](https://github.com/ravellys/GS_produto/blob/main/arquivos/react.gif)

## 🗃 Histórico de lançamentos

* 22/12/2020 Criação do Projeto


## 📋 Meta

Lucas Ravelllys – [Portifólio](https://ravellys.github.io)

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.


## 🚀 Contribuições

1. Faça o _fork_ do projeto (<https://github.com/ravellys/crud-cliente/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_
