from flask import Blueprint, request, jsonify

from app.service.convertes import formatar_numero, to_json
from app.service.file_save import save_json
from app.webscraping import call_webscraping

consumer_controller = Blueprint('consumer', __name__)


@consumer_controller.route('/consulta_processo/1grau',methods=['GET'])
def post_consulta_processo_1grau():
    numero_processo = request.args.get('processo')
    numero_processo_formatado = formatar_numero(numero_processo)
    data = call_webscraping(numero_processo_formatado)
    print("request realizado")
    json_data =  to_json(data)
    save_json(json_data,numero_processo,"results")

    return jsonify(data), 200


@consumer_controller.route('/consulta_processo/2grau',methods=['GET'])
def post_consulta_processo_2grau():
    numero_processo = request.args.get('processo')
    numero_processo_formatado = formatar_numero(numero_processo)
    data = call_webscraping(numero_processo_formatado)
    print("request realizado")
    json_data =  to_json(data)
    save_json(json_data,numero_processo,"results")

    return jsonify(data), 200