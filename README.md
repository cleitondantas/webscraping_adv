# WebScraping-Adv

Um projeto de web scraping em Python utilizando BeautifulSoup4 e Flask, voltado para ler páginas de consultas de processos e retornar os dados em formato JSON.

## 📋 Descrição

O **WebScraping-Adv** é uma aplicação que realiza a extração de dados de páginas de consulta de processos jurídicos. Ele utiliza a biblioteca `BeautifulSoup4` para fazer o parsing do HTML e o `Flask` para fornecer uma API que retorna os dados em formato JSON.

## 🚀 Funcionalidades

- **Web Scraping**: Extrai dados de páginas de consulta de processos.
- **API RESTful**: Expõe os dados extraídos em formato JSON via Flask.
- **Facilidade de Uso**: Basta fornecer a URL da página de consulta para obter os dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **BeautifulSoup4**: Para parsing de HTML.
- **Flask**: Para criar a API web.
- **Requests**: Para fazer requisições HTTP.
- **Poetry**: Para gerenciamento de dependências.

## 📦 Instalação

Siga os passos abaixo para configurar e executar o projeto localmente.

### Pré-requisitos

- Python 3.12
- Poetry (para gerenciamento de dependências)

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/cleitondantas/webscraping_adv.git
   cd webscraping_adv