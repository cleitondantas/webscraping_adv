from bs4 import BeautifulSoup


def header_details(data: dict,soup: BeautifulSoup =None):
    data['numeroProcesso'] = soup.find(id="numeroProcesso").get_text(strip=True) if soup.find(id="numeroProcesso") else None
    data['situacaoProcesso'] = soup.find(id="labelSituacaoProcesso").get_text(strip=True) if soup.find(id="labelSituacaoProcesso") else None
    data['classeProcesso'] = soup.find(id="classeProcesso").get_text(strip=True) if soup.find(id="classeProcesso") else None
    data['assuntoProcesso'] = soup.find(id="assuntoProcesso").get_text(strip=True) if soup.find(id="assuntoProcesso") else None
    data['foroProcesso'] = soup.find(id="foroProcesso").get_text(strip=True) if soup.find(id="foroProcesso") else None
    data['varaProcesso'] = soup.find(id="varaProcesso").get_text(strip=True) if soup.find(id="varaProcesso") else None
    data['juizProcesso'] = soup.find(id="juizProcesso").get_text(strip=True) if soup.find(id="juizProcesso") else None
    data['dataDistribuicao'] = soup.find(id="dataHoraDistribuicaoProcesso").get_text(strip=True) if soup.find(id="dataHoraDistribuicaoProcesso") else None
    data['numeroControleProcesso'] = soup.find(id="numeroControleProcesso").get_text(strip=True) if soup.find(id="numeroControleProcesso") else None
    data['areaProcesso'] = soup.find(id="areaProcesso").get_text(strip=True) if soup.find(id="areaProcesso") else None
    data['valorAcaoProcesso'] = soup.find(id="valorAcaoProcesso").get_text(strip=True) if soup.find(id="valorAcaoProcesso") else None


def tb_partes_principais(data: dict,soup: BeautifulSoup =None):
    partes_processo = []
    partes_table = soup.find("table", id="tablePartesPrincipais")
    if partes_table:
        for row in partes_table.find_all("tr"):
            parte = {}
            tipo = row.find("div", class_="tipoDeParticipacao")
            nome = row.find("td", class_="nomeParteEAdvogado")
            if tipo:
                parte['tipo'] = tipo.get_text(strip=True)
            if nome:
                parte['nome'] = nome.get_text(" ", strip=True)
            if parte:
                partes_processo.append(parte)
    data['partesProcesso'] = partes_processo


def tb_todas_movimentacoes(data: dict,soup: BeautifulSoup =None):
    movimentacoes = []
    movements_table = soup.find("tbody", id="tabelaTodasMovimentacoes")
    if movements_table:
        for row in movements_table.find_all("tr"):
            if "Não há"  in  str(row.find_all("td")[0].get_text(strip=True) if row.find_all("td") else None):
                break
            movimentacao = {}
            data_mov = row.find("td", class_="dataMovimentacao")
            descricao_mov = row.find("td", class_="descricaoMovimentacao")
            if data_mov:
                movimentacao['data'] = data_mov.get_text(strip=True)
            if descricao_mov:
                movimentacao['descricao'] = descricao_mov.get_text(" ", strip=True)
            if movimentacao:
                movimentacoes.append(movimentacao)
    data['movimentacoes'] = movimentacoes


def tb_peticoes_diversas(data: dict,soup: BeautifulSoup =None):
    tables = soup.find_all('table')
    peticoes = []
    data['peticoesdiversas'] = peticoes
    if len(tables) >= 3:
        tbody_peticoesdiversas = tables[2]
        if tbody_peticoesdiversas:
            for row in tbody_peticoesdiversas.find_all("tr"):
                if "Não há"  in  str(row.find_all("td")[0].get_text(strip=True) if row.find_all("td") else None):
                    break
                peticao = {}
                peticao['data'] = row.find_all("td")[0].get_text(strip=True)  if row.find_all("td") else None
                peticao['tipo'] = row.find_all("td")[1].get_text(strip=True) if row.find_all("td") else None
                if peticao.get('tipo') is not None and peticao.get('tipo') != '': # Verifica se o campo está null ou vazio
                    peticoes.append(peticao)


def tb_incidentes(data: dict,soup: BeautifulSoup =None):
    tables = soup.find_all('table')
    incidentes = []
    data['incidentes'] = incidentes
    if len(tables) >= 4:
        tbody_incidentesAcoesIncidentais = tables[3]
        if tbody_incidentesAcoesIncidentais:
            for row in tbody_incidentesAcoesIncidentais.find_all("tr"):
                if "Não há"  in  str(row.find_all("td")[0].get_text(strip=True) if row.find_all("td") else None):
                    break
                incidente = {}
                incidente['data'] = row.find_all("td")[0].get_text(strip=True)  if row.find_all("td") else None
                incidente['tipo'] = str(row.find_all("td")[1].get_text(strip=True)).replace('\n', '').replace('\t', '') if row.find_all("td") else None
                if incidente.get('tipo') is not None and incidente.get('tipo') != '': # Verifica se o campo está null ou vazio
                    incidente['tipo'] = incidente.get('tipo')
                    incidentes.append(incidente)


def tb_items_apensos(data: dict,soup: BeautifulSoup =None):
    tables = soup.find_all('table')
    items_apensos = []
    data['items_apensos'] = items_apensos
    if len(tables) >= 5:
        tbody_apensos_entranhados_unificados = tables[4]
        if tbody_apensos_entranhados_unificados:
            for row in tbody_apensos_entranhados_unificados.find_all("tr"):
                if "Não há"  in  str(row.find_all("td")[0].get_text(strip=True) if row.find_all("td") else None):
                    break

                item = {}
                item['data'] = row.find_all("td")[0].get_text(strip=True)  if row.find_all("td") else None
                item['tipo'] = str(row.find_all("td")[1].get_text(strip=True)).replace('\n', '').replace('\t', '') if row.find_all("td") else None
                if item.get('tipo') is not None and item.get('tipo') != '': # Verifica se o campo está null ou vazio
                    item['tipo'] = item.get('tipo')
                    items_apensos.append(item)