from app.service.convertes import formatar_numero
import unittest
import sys

def test_formatar_numero():
    numero = "10022092920208260161"
    saida = formatar_numero(numero)
    print(saida)
    print("1002209-29.2020.8.26.0161")


if __name__ == '__main__':
   test_formatar_numero()