"""
Carregamento e Limpeza de Dados

Este módulo é responsável por carregar o arquivo CSV de despesas,
realizar a limpeza e preparação dos dados para análise.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from unidecode import unidecode


class DataLoader:
    """Carrega e limpa dados de despesas parlamentares"""
    
    def __init__(self, csv_path: str):
        """
        Inicializa o carregador de dados
        
        Args:
            csv_path: Caminho para o arquivo CSV de despesas
        """
        self.csv_path = Path(csv_path)
        self.df_original = None
        self.df_limpo = None
        
    def carregar_csv(self) -> pd.DataFrame:
        """
        Carrega o arquivo CSV de despesas
        
        Returns:
            DataFrame com os dados originais
            
        Raises:
            FileNotFoundError: Se o arquivo não for encontrado
            pd.errors.EmptyDataError: Se o arquivo estiver vazio
        """
        print(f"\n📂 Carregando arquivo CSV...")
        print(f"   Arquivo: {self.csv_path.name}")
        
        if not self.csv_path.exists():
            raise FileNotFoundError(
                f"❌ Arquivo não encontrado: {self.csv_path}\n"
                f"   Baixe o arquivo em: https://www.camara.leg.br/cota-parlamentar/"
            )
        
        # Carregar CSV com encoding adequado
        try:
            self.df_original = pd.read_csv(
                self.csv_path,
                sep=';',
                encoding='utf-8',
                decimal=',',
                thousands='.',
                dtype={'vlrLiquido': float}
            )
        except UnicodeDecodeError:
            # Tentar outro encoding se UTF-8 falhar
            self.df_original = pd.read_csv(
                self.csv_path,
                sep=';',
                encoding='latin1',
                decimal=',',
                thousands='.',
                dtype={'vlrLiquido': float}
            )
        
        print(f"✅ {len(self.df_original):,} registros carregados")
        print(f"   Colunas disponíveis: {len(self.df_original.columns)}")
        
        return self.df_original
    
    def limpar_dados(self) -> pd.DataFrame:
        """
        Limpa e prepara os dados para análise
        
        Processo de limpeza:
        1. Seleciona apenas colunas necessárias
        2. Remove registros com valores inválidos
        3. Padroniza nomes dos parlamentares
        4. Remove duplicatas
        
        Returns:
            DataFrame limpo e preparado
        """
        print("\n🧹 Limpando dados...")
        
        if self.df_original is None:
            self.carregar_csv()
        
        df = self.df_original.copy()
        
        print(f"   Registros iniciais: {len(df):,}")
        
        # 1. Selecionar apenas colunas necessárias
        colunas_necessarias = ['txNomeParlamentar', 'txtDescricao', 'vlrLiquido']
        
        # Verificar se as colunas existem
        colunas_faltantes = [col for col in colunas_necessarias if col not in df.columns]
        if colunas_faltantes:
            print(f"\n❌ Erro: Colunas não encontradas no CSV: {colunas_faltantes}")
            print(f"   Colunas disponíveis: {list(df.columns)}")
            raise ValueError("Colunas necessárias não encontradas no CSV")
        
        df = df[colunas_necessarias].copy()
        
        # 2. Remover valores inválidos
        # Remove valores nulos
        antes = len(df)
        df = df.dropna(subset=['txNomeParlamentar', 'vlrLiquido'])
        removidos_nulos = antes - len(df)
        
        # Remove valores zero ou negativos
        antes = len(df)
        df = df[df['vlrLiquido'] > 0]
        removidos_invalidos = antes - len(df)
        
        # 3. Padronizar nomes dos parlamentares
        df['txNomeParlamentar'] = df['txNomeParlamentar'].apply(self._padronizar_nome)
        
        # 4. Remover duplicatas (se houver)
        antes = len(df)
        df = df.drop_duplicates()
        removidos_duplicatas = antes - len(df)
        
        # Renomear colunas para facilitar análise
        df = df.rename(columns={
            'txNomeParlamentar': 'nome_deputado',
            'txtDescricao': 'tipo_despesa',
            'vlrLiquido': 'valor'
        })
        
        self.df_limpo = df
        
        # Relatório de limpeza
        print(f"   ✓ Registros removidos (nulos): {removidos_nulos:,}")
        print(f"   ✓ Registros removidos (valores ≤ 0): {removidos_invalidos:,}")
        print(f"   ✓ Registros removidos (duplicatas): {removidos_duplicatas:,}")
        print(f"✅ Registros finais: {len(df):,}")
        print(f"   Redução: {((len(self.df_original) - len(df)) / len(self.df_original) * 100):.1f}%")
        
        return self.df_limpo
    
    @staticmethod
    def _padronizar_nome(nome: str) -> str:
        """
        Padroniza nome do parlamentar para facilitar cruzamento
        
        - Converte para maiúsculas
        - Remove acentos
        - Remove espaços extras
        
        Args:
            nome: Nome original do parlamentar
            
        Returns:
            Nome padronizado
        """
        if pd.isna(nome):
            return ""
        
        # Converter para string e maiúsculas
        nome = str(nome).upper().strip()
        
        # Remover acentos
        nome = unidecode(nome)
        
        # Remover espaços múltiplos
        nome = ' '.join(nome.split())
        
        return nome
    
    def exibir_resumo(self) -> None:
        """Exibe resumo estatístico dos dados"""
        if self.df_limpo is None:
            print("❌ Execute limpar_dados() primeiro")
            return
        
        df = self.df_limpo
        
        print("\n" + "=" * 70)
        print("📊 RESUMO DOS DADOS DE DESPESAS")
        print("=" * 70)
        
        print(f"\n📈 Estatísticas Gerais:")
        print(f"   Total de registros: {len(df):,}")
        print(f"   Total de deputados únicos: {df['nome_deputado'].nunique():,}")
        print(f"   Total de tipos de despesa: {df['tipo_despesa'].nunique():,}")
        print(f"   Valor total das despesas: R$ {df['valor'].sum():,.2f}")
        
        print(f"\n💰 Estatísticas de Valores:")
        print(f"   Média por registro: R$ {df['valor'].mean():,.2f}")
        print(f"   Mediana: R$ {df['valor'].median():,.2f}")
        print(f"   Mínimo: R$ {df['valor'].min():,.2f}")
        print(f"   Máximo: R$ {df['valor'].max():,.2f}")
        
        print(f"\n🏆 Top 10 Tipos de Despesa Mais Comuns:")
        top_despesas = df['tipo_despesa'].value_counts().head(10)
        for i, (tipo, count) in enumerate(top_despesas.items(), 1):
            print(f"   {i}. {tipo}: {count:,} registros")
        
        print(f"\n🏆 Top 10 Deputados com Mais Registros:")
        top_deputados = df['nome_deputado'].value_counts().head(10)
        for i, (nome, count) in enumerate(top_deputados.items(), 1):
            print(f"   {i}. {nome}: {count:,} registros")
        
        print("\n" + "=" * 70)


if __name__ == '__main__':
    # Teste do módulo
    import sys
    
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
        loader = DataLoader(csv_path)
        loader.carregar_csv()
        loader.limpar_dados()
        loader.exibir_resumo()
    else:
        print("Uso: python data_loader.py <caminho_para_csv>")
