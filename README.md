# GS_produto
📜 Este repositório trata-se de um projeto para realizar o CRUD (Create, Read, Update, Delete) de uma entidade Produto com o framework Django. Utilizou-se o método da Class Based Views (CBV) para automatizar e facilitar o encapsulamento das funcionalidades. Para a realização dos testes foi utilizado o pytest-django e como ambiente virtual utilizou-se o pipenv.
** DRF **
** DOCKER **
** React **
Por fim, o projeto foi posto em produção no heroku e para seus arquivos estáticos foi feito um bucket na S3 da amazon. 

link do deploy: [GS_produto](https://gsproduto.herokuapp.com/)

 
## 💻 Configuração para Desenvolvimento

*** Programas necessários

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

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)



### API - Django Rest Framework:


### Consulta da API com  ReactJS:



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
