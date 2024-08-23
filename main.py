from bd import Carros


from flask import Flask, jsonify, request, make_response

# Instancias o modulo flask na nossa variavel app
app = Flask('carros')

# Primeiro metodo - Visualizar os dados(GET)

# app.rout -> definir que essa funcao e uma rota para que o flask entenda que aquilo e um metodo que deve ser executado
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros



# Primeiro metodo pt2- Visulizar os dados por id(GET/ID)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
   for carro in Carros:
       if carro.get('id') == id:
           return jsonify(carro)


# Segundo metodo - Criar novos dados (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem = 'Carro cadastrado com sucesso',
                carro=carro)
    )
# Terceiro metodo - Editar dados (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado =request.get_json()
    for indice,carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])


# Quarto metodo - Deletar dados(DELETE)
@app.route('/carros/<int:id>', methods =['DElETE'])
def excluir_carro(id):
    for indice,carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem":"Carro excluido com sucesso"})





app.run(port=5000, host='localhost')