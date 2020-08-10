# gerenciamento_funcionario
## Installation / Usage

#### Dependência
* Será necessário criar um ambiente virtual e preparalo com a instalação do requirements:
    ```
    $ pip install -r requirements.txt
    ```

#### Executando o sistema em seu localhost
* Crie seu banco de dados e execute os passos abaixo:
    * Necessário ter um database chamado 'localdb'
    ```
    $ python manage.py migrate
    ```
    ```
    $ python manage.py runserver
    ```
    ```
    $ python manage.py createsuperuser
    ```

#### Executando tests
    ```
    $ python manage.py test
    ```
#### Endpoints

* **Você porderá executar do Heroku ou local**

* Base endpoint:
    
        http://hero-company.herokuapp.com/
        http://localhost:8000/
        http://127.0.0.1:8000/
    
* Endpoint de funcionarios:
    * listagem de todos os funcionarios:
        $url-to-api/funcionario/ - GET

        * resposta:
                    [
                    {
                        "first_name": "str",
                        "last_name": "str",
                        "email": "str",
                        "cargo": "str",
                        "idade": int,
                        "username": "str",
                        "empresa": list
                    }
                ]

    * listagem de um funcionario especifico:
        $url-to-api/funcionario/<username> - GET

        * resposta:
                    {
                        "first_name": "str",
                        "last_name": "str",
                        "email": "str",
                        "cargo": "str",
                        "idade": int,
                        "username": "str",
                        "empresa": list
                    }
    
    * criação de um funcionario:
        $url-to-api/funcionario/ - POST

        * dados de envio para criação do funcionario:
                    {
                        "first_name": "str",
                        "last_name": "str",
                        "email": "str",
                        "cargo": "str",
                        "idade": int,
                        "username": "str",
                        "empresa": list (podendo passar vazio)
                    }

        * resposta:
                    {
                        "first_name": "str",
                        "last_name": "str",
                        "email": "str",
                        "cargo": "str",
                        "idade": int,
                        "username": "str",
                        "empresa": list
                    }

    * update de um funcionario especifico:
        $url-to-api/funcionario/<username> - PATCH

        * dados de envio para atualização do funcionario:
                    {
                        "campos que serão alterados": "valor alterado"
                    }

        * resposta:
                    {
                        "first_name": "str",
                        "last_name": "str",
                        "email": "str",
                        "cargo": "str",
                        "idade": int,
                        "username": "str",
                        "empresa": list
                    }
        
    * deleção de um funcionario especifico:
        $url-to-api/funcionario/<username> - DELETE

        * este endpoint não retornará uma response

* Endpoint de empresas:
    * listagem de todas as empresas:
        $url-to-api/empresa/ - GET

        * resposta:
                    [
                    {
                        "nome_fantasia": "str",
                        "localizacao": "str",
                        "razao_social": "str",
                        "cnpj": "str",
                        "funcionarios": list
                    }
                ]

    * listagem de uma empresa especifica:
        $url-to-api/empresa/<razao_social> - GET

        * resposta:
                    {
                        "nome_fantasia": "str",
                        "localizacao": "str",
                        "razao_social": "str",
                        "cnpj": "str",
                        "funcionarios": list
                    }
    
    * criação de um funcionario:
        $url-to-api/empresa/ - POST

        * dados de envio para criação da empresa:
                    {
                        "nome_fantasia": "str",
                        "localizacao": "str",
                        "razao_social": "str",
                        "cnpj": "str",
                        "funcionarios": list (podendo passar vazio)
                    }

        * resposta:
                    {
                        "nome_fantasia": "str",
                        "localizacao": "str",
                        "razao_social": "str",
                        "cnpj": "str",
                        "funcionarios": list
                    }

    * update de uma empresa especifica:
        $url-to-api/funcionario/<username> - PATCH

        * dados de envio para atualização da empresa:
                    {
                        "campos que serão alterados": "valor alterado"
                    }

        * resposta:
                    {
                        "nome_fantasia": "str",
                        "localizacao": "str",
                        "razao_social": "str",
                        "cnpj": "str",
                        "funcionarios": list
                    }
        
    * deleção de um funcionario especifico:
        $url-to-api/funcionario/<username> - DELETE

        * este endpoint não retornará uma response

#### Status table

| Code | Status |
|:-------:|:---------:|
| 200   | OK |
| 201   | CREATED |
| 204   | NO_CONTENT |
| 400   | BAD_REQUEST |
| 404   | NOT_FOUND |
| 405   | METHOD_NOT_ALLOWED |
