from app.modules.esaj_tjsp.cons_1grau import *
from app.service.convertes import to_json
from app.service.request_service import get_request


#numero_processo = "1007754-73.2021.8.26.015"

# URL Segunda instancia
# url: str ="https://esaj.tjsp.jus.br/cposg/search.do?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado=&foroNumeroUnificado=&dePesquisaNuUnificado=&dePesquisaNuUnificado=UNIFICADO&dePesquisa="+numero_processo+"&tipoNuProcesso=SAJ#"

def call_webscraping(numero_processo : str):
    url: str ="https://esaj.tjsp.jus.br/cpopg/search.do?conversationId=&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado=&foroNumeroUnificado=&dadosConsulta.valorConsultaNuUnificado=&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta="+numero_processo+"&dadosConsulta.tipoNuProcesso=SAJ"
    print(url)
    data = {}
    soup = get_request(url=url)
    header_details(data,soup)
    tb_partes_principais(data,soup)
    tb_todas_movimentacoes(data,soup)
    tb_peticoes_diversas(data,soup)
    tb_incidentes(data,soup)
    tb_items_apensos(data,soup)
    return data



