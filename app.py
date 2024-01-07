from flask import Flask, jsonify, request

# Instanciando a classe
app = Flask(__name__)

livros = [
  {
    'id': 1,
    'título': 'Tudo é Rio',
    'autora': 'Carla Madeira'
  },
  {
    'id': 2,
    'título': 'A Hora da Estrela',
    'autora': 'Clarice Lispector'
  },
  {
    'id': 3,
    'título': 'Rita Lee: Outra autobiografia',
    'autora': 'Rita Lee'
  }
]

# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
  novo_livro = request.get_json()
  livros.append(novo_livro)
  return jsonify(livros), 201

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
  return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
  for livro in livros:
    if livro.get('id') == id:
      return jsonify(livro)
    
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
  livro_alterado = request.get_json()
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      del livros[indice]
  return jsonify(livros)

# Iniciando o serviço
app.run(port=5500, host='localhost', debug=True)