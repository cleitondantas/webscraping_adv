import requests
from bs4 import BeautifulSoup


def get_request(url):
    try:
        response = requests.get(url, timeout=10)
        return BeautifulSoup(response.content, 'html.parser')
    except requests.exceptions.RequestException as e:
        return f"error: {str(e)}"