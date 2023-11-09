# CRUD API and Interface

Este repositório contém uma aplicação para realizar operações CRUD (Create, Read, Update, Delete) em uma tabela de pessoas. A aplicação consiste em uma REST API para o backend e uma interface simples para interação com o usuário.

## Tecnologias Utilizadas

### Backend
- Linguagem: Python 3
- Framework: Flask (micro framework)
- Banco de Dados: MySQL
- Arquivos Python -
      Frameworks - flask, request,jsonify, mysqlconnector, flask_cors, datetime, render_template, requests, Mysqlconnector, pytest, json.

### Frontend
- HTML5
- CSS (utilizando Bulma framework)

## Instruções de Uso

### Configuração do Ambiente

1. Certifique-se de ter o Python 3 instalado em seu sistema.
2. Execute o script Iport_MySql.py fornecido para criar a tabela e popular dados iniciais.

### Iniciando o Backend

1. execute o seguinte comando:
   ```
   python Api.py
   ```
   ````
   python Client.py
   ```
   \\Isso iniciará o servidor Flask.

### Iniciando o Frontend

1. Navegue até a pasta `Tamplates` e abra o arquivo `index.html` em seu navegador.

# Testes 

1. para executar os testes de API, no prompt de comando, e execute o comando pytest testes.py 

## Funcionalidades da Aplicação

### 1. Tela "Índice"

- Listagem de registros da tabela "pessoas" com colunas "nome" e "data de admissão".
- Botões para "Ver Mais", "Editar" e "Excluir" para cada registro.
- Adição de novo registro através do botão "Adicionar Registro".

### 2. Tela "Registro Selecionado"

- Exibição completa dos dados do registro selecionado.
- Botões "Editar" e "Excluir" para interações adicionais.

### 3. Tela "Atualizar Dados de Registro"

- Formulário preenchido com dados atuais do registro.
- Botão "Cancelar" para retornar à listagem sem efetuar mudanças.
- Botão "Salvar" para gravar a inclusão.

### 4. Tela "Adicionar Registro"

- Formulário para adição de novo registro.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias.

## Autor

Daiany Sobreira
