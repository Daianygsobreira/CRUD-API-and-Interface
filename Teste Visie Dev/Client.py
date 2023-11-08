from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Rota pagina inicial, listando as pessoas.
@app.route('/')
def index():
    return render_template('Indice.html')

# Rota pagina para adicionar pessoas.
@app.route('/inclusao_pessoa/', methods=['GET'])
def inclusao_pessoa():
    return render_template('Adicionar_pessoa.html')

# Rota para pagina de detalhes da pessoa selecionada.
@app.route('/detalhes/<int:id_pessoa>', methods=['GET'])
def detalhes_pessoa(id_pessoa):
    try:
        api_url = f'http://127.0.0.1:5001/Api/detalhes_pessoa/{id_pessoa}'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            pessoa = response.json()
            return render_template('Detalhes_pessoa.html', pessoa=pessoa)
        else:
            return "Pessoa não encontrada.", 404
    except Exception as e:
        return str(e)

# Rota para a pagina de alteração dos dados da pessoa.    
@app.route('/atualizar_pessoa/<int:id_pessoa>', methods=['GET'])
def exibir_formulario_atualizacao(id_pessoa):
    try:
        api_url = f'http://127.0.0.1:5001/Api/detalhes_pessoa/{id_pessoa}'
        response = requests.get(api_url)

        if response.status_code == 200:
            pessoa = response.json()
            return render_template('Atualizar_pessoa.html', pessoa=pessoa)
        else:
            return "Pessoa não encontrada.", 404
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
