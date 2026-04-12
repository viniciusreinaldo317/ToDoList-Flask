from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
tarefaId = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global tarefaId
    data = request.get_json()

    nova_tarefa = Task(id = tarefaId, title = data.get("title"), description = data.get("description", ""))

    tarefaId +=1

    tasks.append(nova_tarefa)
    print(tasks)

    return jsonify({"message": "nova tarefa criada com sucesso!"})

@app.route('/tasks', methods=['GET'])
def get_tarefa():
    lista_de_tarefa = []
    for tarefa in tasks:
        lista_de_tarefa.append(tarefa.retornoDict())


    saida = {
        "tarefa": lista_de_tarefa,
        "total_tarefa": len(lista_de_tarefa)
    }

    return jsonify(saida)

@app.route('/tasks/<int:id>', methods=['GET'])
def listaPorId(id):
    for tarefaId in tasks:
        if tarefaId.id == id:
            return jsonify(tarefaId.retornoDict())

        return jsonify({"message": "Não foi possivel encontar a atividade"}), 404

@app.route('/task/<int:id>', methods=['PUT'])
def atualizar(id):
    task = None
    for atu in tasks:
        if atu.id == id:
            task = atu
            break
    print(task)
    if task == None:
        return jsonify({"message": "não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)

    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tas/<int:id>', methods=['DELETE'])
def remover(id):
    task = None
    for remov in tasks:
        if remov.id == id:
            task = remov
            break

        if remov == None:
            return jsonify({"message": "Tarefa não encontrada"}), 404
        
        tasks.remove(task)
        return jsonify({"message": "Tarefa deletada com sucesso"})
    

if __name__ == "__main__":
    app.run(debug=True)