"""
Cliente para API de Dados Abertos da Câmara dos Deputados

Este módulo fornece uma interface simples para buscar dados cadastrais
dos deputados federais em exercício.
"""

import requests
import pandas as pd
from typing import Dict, List


class CamaraAPI:
    """Cliente para consulta à API de Dados Abertos da Câmara dos Deputados"""
    
    BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json',
            'User-Agent': 'AnaliseGastosParlamentares/1.0'
        })
    
    def buscar_deputados(self) -> pd.DataFrame:
        """
        Busca lista de todos os deputados em exercício
        
        Returns:
            DataFrame com colunas: nome, siglaPartido, siglaUf
            
        Raises:
            requests.exceptions.RequestException: Se houver erro na requisição
        """
        print("🌐 Buscando dados dos deputados na API...")
        
        try:
            url = f"{self.BASE_URL}/deputados"
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            deputados = data.get('dados', [])
            
            # Criar DataFrame com apenas as colunas necessárias
            df = pd.DataFrame(deputados)
            df = df[['nome', 'siglaPartido', 'siglaUf']].copy()
            
            print(f"✅ {len(df)} deputados encontrados")
            
            return df
            
        except requests.exceptions.Timeout:
            print("❌ Erro: Timeout ao conectar com a API")
            raise
        except requests.exceptions.ConnectionError:
            print("❌ Erro: Não foi possível conectar à API. Verifique sua conexão.")
            raise
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao buscar deputados: {e}")
            raise
    
    def exibir_exemplo_dados(self) -> None:
        """Exibe um exemplo dos dados retornados pela API"""
        try:
            df = self.buscar_deputados()
            print("\n📊 Exemplo de dados da API:")
            print("-" * 60)
            print(df.head(10).to_string(index=False))
            print("-" * 60)
            
            print("\n📈 Resumo dos dados:")
            print(f"  - Total de deputados: {len(df)}")
            print(f"  - Total de partidos: {df['siglaPartido'].nunique()}")
            print(f"  - Total de estados: {df['siglaUf'].nunique()}")
            
            print("\n📊 Deputados por partido (Top 10):")
            print(df['siglaPartido'].value_counts().head(10))
            
        except Exception as e:
            print(f"❌ Erro ao exibir exemplo: {e}")


if __name__ == '__main__':
    # Teste do módulo
    api = CamaraAPI()
    api.exibir_exemplo_dados()
