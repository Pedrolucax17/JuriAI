import json
import requests 
from .literals import TribunalLiteral
from agno.tools import tool

@tool
def search_datajud_api(tribunal: TribunalLiteral, process_number: str) -> str:
  """
    Busca informações de um processo judicial na API pública do DataJud (CNJ).
    
    Realiza uma consulta na API pública do Conselho Nacional de Justiça
    para obter dados de um processo judicial específico em um determinado tribunal.
    
    Args:
        tribunal: Código do tribunal onde o processo está tramitando.
            Valores aceitos: "tst", "tse", "stj", "stm", "trf1"-"trf6", 
            "tjsp", "tjmg", etc. (ver TribunalLiteral para lista completa).
        process_number: Número do processo judicial no formato CNJ
            (ex: "00008323520184013202").
    
    Returns:
        Resposta da API em formato JSON como string contendo os dados do processo,
        incluindo informações como número, partes, movimentações, decisões, etc.
        Retorna JSON com campo "error" em caso de falha na requisição.
    """

  url = f"https://api-publica.datajud.cnj.jus.br/api_publica_{tribunal}/_search"
  payload = {
    "query": {
      "match": {
        "numeroProcesso": process_number
      }
    }
  }
  headers = {
    #apiKey publica na dodcumentação do cnj
    "Authorization": f"APIKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==",
    "Content-Type": "application/json"
  }
  
  try:
    response = requests.post(url, headers=headers, json=payload)
    return response.text
  except requests.RequestException as e:
    return f'Erro: {e}'