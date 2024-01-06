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

# Comsultar (todos)
# decorator para atribuir a rota
@app.route('/livros', methods=['GET'])
def obter_livros():
  return jsonify(livros)

# Consultar (id)
# Editar
# Excluir

# Iniciando o serviço
app.run(port=5500, host='localhost', debug=True)