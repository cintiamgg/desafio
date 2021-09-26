# -*- coding: utf-8 -*-
import json
import csv
from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

ipServidorAPI = "192.168.15.16"
portaServidorAPI = "8095"

app = Flask(__name__)
CORS(app)
api = Api(app)

class getData(Resource):
    def post(self):
        x = request.stream.read()
        y = json.loads(x)

        ip = y["ip"]
        data = datetime.today().strftime('%Y_%m_%d')
        nomeDoArquivo = ip+"_"+data+".csv"
        
        processador = y["processador"].replace(",","")
        sistemaOperacional = y["sistemaOperacional"].replace(",","")
        versaoSistemaOperacional = y["versaoSistemaOperacional"].replace(",","")
        usuarios = y["usuarios"]
        processos = y["processos"]
        
        header = ['processador', 'sistemaOperacional', 'versaoSistemaOperacional', 'usuarios', 'processos']
        dados = []
        dados.append([processador, sistemaOperacional, versaoSistemaOperacional, usuarios, processos]                )
                
        with open(nomeDoArquivo, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(dados)

api.add_resource(getData, '/data') 

if __name__ == '__main__':
    app.run(host=ipServidorAPI, port=portaServidorAPI, threaded=False)
   


