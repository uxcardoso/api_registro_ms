from settings import Resource, api, jsonify
from crawlers.ms_crawler import MsCrawler

class Index(Resource):
    def get(self):
        return {"menssagem": "Bem Vindo a API Registro MS"}

class GetMS(Resource):
    def get(self, num_ms):
        ms = MsCrawler()
        response = ms.get_medicines(num_ms)
        return jsonify({"resposta_medicamento": response})



api.add_resource(Index, "/")
api.add_resource(GetMS, "/codigo_ms/<num_ms>")