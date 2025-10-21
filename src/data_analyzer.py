"""
Análise e Cruzamento de Dados

Este módulo realiza o cruzamento entre os dados de despesas (CSV)
e os dados cadastrais dos deputados (API), gerando análises agregadas.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from unidecode import unidecode


class DataAnalyzer:
    """Analisa e cruza dados de despesas com dados cadastrais"""
    
    def __init__(self, df_despesas: pd.DataFrame, df_deputados: pd.DataFrame):
        """
        Inicializa o analisador
        
        Args:
            df_despesas: DataFrame com despesas (do CSV)
            df_deputados: DataFrame com dados cadastrais (da API)
        """
        self.df_despesas = df_despesas.copy()
        self.df_deputados = df_deputados.copy()
        self.df_cruzado = None
        
    def cruzar_dados(self) -> pd.DataFrame:
        """
        Cruza dados de despesas com dados cadastrais dos deputados
        
        Utiliza o nome do parlamentar como chave de ligação.
        Deputados não identificados são marcados como "NÃO IDENTIFICADO".
        
        Returns:
            DataFrame com dados cruzados
        """
        print("\n🔗 Cruzando dados de despesas com dados cadastrais...")
        
        # Padronizar nomes dos deputados na API também
        self.df_deputados['nome_padrao'] = self.df_deputados['nome'].apply(
            self._padronizar_nome
        )
        
        # Criar coluna auxiliar para o join
        despesas = self.df_despesas.copy()
        despesas['nome_padrao'] = despesas['nome_deputado']
        
        # Left join: mantém todas as despesas
        df_merged = despesas.merge(
            self.df_deputados[['nome_padrao', 'siglaPartido', 'siglaUf']],
            on='nome_padrao',
            how='left'
        )
        
        # Renomear colunas
        df_merged = df_merged.rename(columns={
            'siglaPartido': 'partido',
            'siglaUf': 'uf'
        })
        
        # Marcar deputados não identificados
        df_merged['partido'] = df_merged['partido'].fillna('NÃO IDENTIFICADO')
        df_merged['uf'] = df_merged['uf'].fillna('NÃO IDENTIFICADO')
        
        # Remover coluna auxiliar
        df_merged = df_merged.drop('nome_padrao', axis=1)
        
        self.df_cruzado = df_merged
        
        # Relatório do cruzamento
        total_despesas = len(df_merged)
        identificados = len(df_merged[df_merged['partido'] != 'NÃO IDENTIFICADO'])
        nao_identificados = total_despesas - identificados
        taxa_identificacao = (identificados / total_despesas) * 100
        
        print(f"✅ Cruzamento concluído!")
        print(f"   Total de registros: {total_despesas:,}")
        print(f"   Identificados: {identificados:,} ({taxa_identificacao:.1f}%)")
        print(f"   Não identificados: {nao_identificados:,} ({100-taxa_identificacao:.1f}%)")
        
        if nao_identificados > 0:
            print(f"\n⚠️  Deputados não identificados:")
            nomes_nao_ident = df_merged[df_merged['partido'] == 'NÃO IDENTIFICADO']['nome_deputado'].unique()
            for nome in nomes_nao_ident[:10]:  # Mostrar apenas 10
                print(f"      - {nome}")
            if len(nomes_nao_ident) > 10:
                print(f"      ... e mais {len(nomes_nao_ident) - 10}")
        
        return self.df_cruzado
    
    def analisar_por_partido(self) -> pd.DataFrame:
        """
        Agrega gastos por partido político
        
        Returns:
            DataFrame com análise por partido
        """
        print("\n📊 Analisando gastos por partido...")
        
        if self.df_cruzado is None:
            self.cruzar_dados()
        
        # Remover não identificados para esta análise
        df = self.df_cruzado[self.df_cruzado['partido'] != 'NÃO IDENTIFICADO'].copy()
        
        # Agregações por partido
        analise_partido = df.groupby('partido').agg({
            'valor': ['sum', 'mean', 'median', 'count'],
            'nome_deputado': 'nunique'
        }).round(2)
        
        # Renomear colunas
        analise_partido.columns = [
            'total_gasto', 'gasto_medio', 'gasto_mediano', 
            'num_registros', 'num_deputados'
        ]
        
        # Calcular média por deputado
        analise_partido['media_por_deputado'] = (
            analise_partido['total_gasto'] / analise_partido['num_deputados']
        ).round(2)
        
        # Ordenar por total gasto
        analise_partido = analise_partido.sort_values('total_gasto', ascending=False)
        
        print(f"✅ {len(analise_partido)} partidos analisados")
        
        return analise_partido.reset_index()
    
    def analisar_por_estado(self) -> pd.DataFrame:
        """
        Agrega gastos por estado (UF)
        
        Returns:
            DataFrame com análise por estado
        """
        print("\n📊 Analisando gastos por estado...")
        
        if self.df_cruzado is None:
            self.cruzar_dados()
        
        # Remover não identificados
        df = self.df_cruzado[self.df_cruzado['uf'] != 'NÃO IDENTIFICADO'].copy()
        
        # Agregações por UF
        analise_uf = df.groupby('uf').agg({
            'valor': ['sum', 'mean', 'median', 'count'],
            'nome_deputado': 'nunique'
        }).round(2)
        
        # Renomear colunas
        analise_uf.columns = [
            'total_gasto', 'gasto_medio', 'gasto_mediano',
            'num_registros', 'num_deputados'
        ]
        
        # Calcular média por deputado
        analise_uf['media_por_deputado'] = (
            analise_uf['total_gasto'] / analise_uf['num_deputados']
        ).round(2)
        
        # Ordenar por total gasto
        analise_uf = analise_uf.sort_values('total_gasto', ascending=False)
        
        print(f"✅ {len(analise_uf)} estados analisados")
        
        return analise_uf.reset_index()
    
    def analisar_tipos_despesa(self) -> pd.DataFrame:
        """
        Agrega gastos por tipo de despesa
        
        Returns:
            DataFrame com análise por tipo de despesa
        """
        print("\n📊 Analisando tipos de despesa...")
        
        if self.df_cruzado is None:
            self.cruzar_dados()
        
        df = self.df_cruzado[self.df_cruzado['partido'] != 'NÃO IDENTIFICADO'].copy()
        
        # Agregações por tipo de despesa
        analise_despesa = df.groupby('tipo_despesa').agg({
            'valor': ['sum', 'mean', 'count']
        }).round(2)
        
        # Renomear colunas
        analise_despesa.columns = ['total_gasto', 'gasto_medio', 'num_registros']
        
        # Calcular percentual do total
        total_geral = analise_despesa['total_gasto'].sum()
        analise_despesa['percentual'] = (
            (analise_despesa['total_gasto'] / total_geral) * 100
        ).round(2)
        
        # Ordenar por total gasto
        analise_despesa = analise_despesa.sort_values('total_gasto', ascending=False)
        
        print(f"✅ {len(analise_despesa)} tipos de despesa analisados")
        
        return analise_despesa.reset_index()
    
    def analisar_top_deputados(self, top_n: int = 20) -> pd.DataFrame:
        """
        Identifica deputados com maiores gastos
        
        Args:
            top_n: Número de deputados a retornar
            
        Returns:
            DataFrame com top deputados
        """
        print(f"\n📊 Analisando top {top_n} deputados com maiores gastos...")
        
        if self.df_cruzado is None:
            self.cruzar_dados()
        
        df = self.df_cruzado[self.df_cruzado['partido'] != 'NÃO IDENTIFICADO'].copy()
        
        # Agregações por deputado
        top_deputados = df.groupby(['nome_deputado', 'partido', 'uf']).agg({
            'valor': ['sum', 'count']
        }).round(2)
        
        # Renomear colunas
        top_deputados.columns = ['total_gasto', 'num_registros']
        
        # Ordenar e pegar top N
        top_deputados = top_deputados.sort_values('total_gasto', ascending=False).head(top_n)
        
        print(f"✅ Top {top_n} deputados identificados")
        
        return top_deputados.reset_index()
    
    def gerar_relatorio_completo(self) -> dict:
        """
        Gera relatório completo com todas as análises
        
        Returns:
            Dicionário com todos os DataFrames de análise
        """
        print("\n" + "=" * 70)
        print("📊 GERANDO RELATÓRIO COMPLETO")
        print("=" * 70)
        
        relatorio = {
            'dados_cruzados': self.cruzar_dados(),
            'por_partido': self.analisar_por_partido(),
            'por_estado': self.analisar_por_estado(),
            'por_tipo_despesa': self.analisar_tipos_despesa(),
            'top_deputados': self.analisar_top_deputados()
        }
        
        print("\n" + "=" * 70)
        print("✅ RELATÓRIO COMPLETO GERADO")
        print("=" * 70)
        
        return relatorio
    
    @staticmethod
    def _padronizar_nome(nome: str) -> str:
        """Padroniza nome para cruzamento"""
        if pd.isna(nome):
            return ""
        nome = str(nome).upper().strip()
        nome = unidecode(nome)
        nome = ' '.join(nome.split())
        return nome


if __name__ == '__main__':
    print("Este módulo deve ser importado, não executado diretamente.")
    print("Use: from data_analyzer import DataAnalyzer")
