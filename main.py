"""Arquivo main da API"""
from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask_cors import CORS
import firebase_admin
from firebase_admin import firestore


# Aqui iniciamos a API
app = Flask(__name__)
CORS(app)
API = Api(app)


# Iniciando o firebase com as credenciais que você salvou na raiz da aplicação no passo 3.1
# Não se esqueça de colocar o nome do arquivo que você salvou, no meu caso esta com o nome de "kevy-petstore-angular-firebase-adminsdk-nl3vp-44948ae1bc"

cred = firebase_admin.credentials.Certificate(
    './kevy-petstore-angular-firebase-adminsdk-nl3vp-44948ae1bc.json')

firebase_admin.initialize_app(credential=cred)
FIRESTORE_DB = firestore.client()

@app.before_request
def start_request():
    """Start api request"""
    if request.method == 'OPTIONS':
        return '', 200
    if not request.endpoint:
        return 'Sorry, Nothing at this URL.', 404


# Nossa classe principal
class Index(Resource):
    """ class return API index """

    def get(self):
        """return API"""
        return {"API": "Heroes"}


# Nossa primeira url
API.add_resource(Index, '/', endpoint='index')


if __name__ == '__main__':
    # Isso é utilizado somente para executar a aplicação local. Quando
    # realizarmos o deploy para o Google App Engine, o webserver deles ira
    # iniciar a aplicação de outra forma
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
