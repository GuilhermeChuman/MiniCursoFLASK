from flask import Flask, jsonify, request
from flask_cors import CORS
import data_loader as dl

app = Flask(__name__)

CORS(app)

@app.route("/")
def inicio():
    return "Minha primeira aplicação Flask!"

@app.route("/sobre")
def sobre():
    return "API desenvolvida com Flask"

@app.route("/versao")
def versao():
    return "Versão 1.0"

@app.route("/addAluno", methods = ["POST"])
def addAluno():
    data = request.get_json()
    if dl.addAluno(data):
        return jsonify({"mensagem": "Aluno cadastrado!"}), 201

@app.route("/deleteAluno/<int:idAluno>", methods = ["DELETE"])
def deleteAluno(idAluno):
    if dl.deleteAluno(idAluno):
        return jsonify({"mensagem": "Aluno excluído!"}), 201
    
@app.route("/updateAluno/<int:idAluno>", methods = ["PUT"])
def updateAluno(idAluno):
    data = request.get_json()
    if dl.updateAluno(idAluno, data):
        return jsonify({"mensagem": "Registro atualizado!"}), 201

@app.route("/loadAlunos", methods = ["GET"])
def loadAlunos():
    response = dl.loadAlunos()
    return jsonify({"response": response}), 201

@app.route("/buscaAluno/<string:term>", methods = ["GET"])
def searchAlunoByName(term):
    response = dl.searchAlunoByName(term)
    return jsonify({"response": response}), 201

if __name__ == "__main__":
    app.run(debug=True)

