import pytest
import json
from Api import app

# Fixture para o aplicativo Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

# Teste para listar todas as pessoas
def test_listar_pessoas(client):
    response = client.get('/Api/pessoas')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

# Teste para listar detalhes de uma pessoa que existe
def test_obter_detalhes_pessoa_existente(client):
    response = client.get('/Api/detalhes_pessoa/2')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, dict)

# Teste para listar detalhes de uma pessoa que não existe
def test_obter_detalhes_pessoa_inexistente(client):
    response = client.get('/Api/detalhes_pessoa/999')  # Supondo que o ID 999 não existe
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data

# Teste para adicionar uma pessoa
def test_adicionar_pessoa(client):
    pessoa_data = {
        'nome': 'Novo Nome',
        'rg': '123456789',
        'cpf': '987654321',
        'data_nascimento': '01/01/1990',
        'data_admissao': '01/01/2023',
        'funcao': 'Programador'
    }
    response = client.post('/Api/add_pessoas/', data=pessoa_data)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'messagem' in data

# Teste para atualizar os dados de uma pessoa
def test_atualizar_pessoa(client):
    pessoa_data = {
        'nome': 'Nome Atualizado',
        'rg': '123456789',
        'cpf': '987654321',
        'data_nascimento': '01/01/1990',
        'data_admissao': '01/01/2023',
        'funcao': 'Programador'
    }
    response = client.post('/Api/atualizar_pessoa/23', data=pessoa_data)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data

# Teste para excluir uma pessoa
def test_excluir_pessoa(client):
    response = client.delete('/Api/delete_pessoas/23')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data

if __name__ == '__main__':
    pytest.main()
