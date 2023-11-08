from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configuração do banco de dados
db_config = {
    "host": "jobs.visie.com.br",
    "user": "daianygoncalves",
    "password": "ZGFpYW55Z29u",
    "database": "daianygoncalves",
    "port":"3306"
}

# Função para conectar ao banco de dados
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Função para formatar datas no formato brasileiro
def formatar_data_brasileira(data):
    if data:
        return data.strftime('%d/%m/%Y')
    return None

# Rota para listar todas as pessoas
@app.route('/Api/pessoas', methods=['GET'])
def listar_pessoas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id_pessoa, nome, DATE_FORMAT(data_admissao, '%d/%m/%Y') as data_admissao FROM pessoas")
        pessoas = cursor.fetchall()
        conn.close()

        return jsonify(pessoas)
    except Exception as e:
        return jsonify({"error": str(e)})
    
# Rota para listar detalhes das pessoas.
@app.route('/Api/detalhes_pessoa/<int:id_pessoa>', methods=['GET'])    
def obter_detalhes_pessoa(id_pessoa):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pessoas WHERE id_pessoa = %s", (id_pessoa,))
        pessoa = cursor.fetchone()
        conn.close()
        if pessoa:
            pessoa['data_admissao'] = formatar_data_brasileira(pessoa['data_admissao'])
            pessoa['data_nascimento'] = formatar_data_brasileira(pessoa['data_nascimento'])
            return jsonify(pessoa)
        else:
            return jsonify({"error": "Pessoa não encontrada."}), 404
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para adicionar uma pessoa
@app.route('/Api/add_pessoas/', methods=['POST'])
def adicionar_pessoa():
        nome = request.form.get('nome')
        rg = request.form.get('rg')
        cpf = request.form.get('cpf')
        data_nascimento = request.form.get('data_nascimento')
        data_admissao = request.form.get('data_admissao')
        funcao = request.form.get('funcao')

        try:
            data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
            data_admissao = datetime.strptime(data_admissao, '%d/%m/%Y').strftime('%Y-%m-%d')
    
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pessoas (nome, rg, cpf, data_nascimento, data_admissao, funcao) VALUES (%s, %s, %s, %s, %s, %s)",
                        (nome, rg, cpf, data_nascimento, data_admissao, funcao))
            conn.commit()
            conn.close()
            return jsonify({"messagem": "Pessoa adicionada com sucesso."}), 201
        except Exception as e:
            return jsonify({"error": str(e)})


# Rota para atualizar os dados de uma pessoa
@app.route('/Api/atualizar_pessoa/<int:id_pessoa>', methods=['POST'])
def atualizar_dados_pessoa(id_pessoa):

    nome = request.form.get('nome')
    rg = request.form.get('rg')
    cpf = request.form.get('cpf')
    data_nascimento = request.form.get('data_nascimento')
    data_admissao = request.form.get('data_admissao')
    funcao = request.form.get('funcao')

    try:
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
        data_admissao = datetime.strptime(data_admissao, '%d/%m/%Y').strftime('%Y-%m-%d')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE pessoas SET nome = %s, rg = %s, cpf = %s, data_nascimento = %s, data_admissao = %s, funcao = %s WHERE id_pessoa = %s",
                    (nome, rg, cpf, data_nascimento, data_admissao, funcao, id_pessoa))
        conn.commit()
        conn.close()
        return jsonify({"message": "Pessoa atualizada com sucesso."})
    except Exception as e:
        return jsonify({"error": str(e)})

# Rota para excluir uma pessoa
@app.route('/Api/delete_pessoas/<int:id_pessoa>', methods=['DELETE'])
def excluir_pessoa(id_pessoa):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pessoas WHERE id_pessoa = %s", (id_pessoa,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Pessoa excluída com sucesso."})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
