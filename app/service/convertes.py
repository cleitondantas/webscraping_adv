import json

def to_json(data = dict):
    return json.dumps(data, ensure_ascii=False, indent=4)

def formatar_numero(numero):
  """Formata um número inteiro longo com pontos e traços.

  Args:
    numero: O número inteiro a ser formatado.

  Returns:
    Uma string com o número formatado.
  """
  # Convertendo o número para string para manipulação

  numero_str = str(numero)
  if(numero_str.isdigit()):
      # Separando os dígitos em grupos
      # 1002209-29.2020.8.26.0161
      # 10022092920208260161
      grupo1 = numero_str[:7]
      grupo2 = numero_str[7:9]
      grupo3 = numero_str[9:13]
      grupo4 = numero_str[13:14]
      grupo5 = numero_str[14:16]
      grupo6 = numero_str[16:20]

      # Juntando os grupos com os separadores
      numero_formatado = f"{grupo1}-{grupo2}.{grupo3}.{grupo4}.{grupo5}.{grupo6}"
      return numero_formatado
  else:
    return numero_str