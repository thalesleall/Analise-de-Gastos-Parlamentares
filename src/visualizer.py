"""
Visualização de Dados

Este módulo gera gráficos e visualizações das análises realizadas.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


class Visualizer:
    """Gera visualizações das análises de gastos parlamentares"""
    
    def __init__(self, output_dir: str = 'resultados'):
        """
        Inicializa o visualizador
        
        Args:
            output_dir: Diretório para salvar os gráficos
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Configurar estilo dos gráficos
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette('husl')
        
        # Configurar cores
        self.colors = sns.color_palette('husl', 15)
    
    def plot_gastos_partido(self, df_partido: pd.DataFrame, top_n: int = 15) -> None:
        """
        Gera gráfico de gastos por partido
        
        Args:
            df_partido: DataFrame com análise por partido
            top_n: Número de partidos a exibir
        """
        print(f"\n📊 Gerando gráfico: Gastos por Partido (Top {top_n})...")
        
        # Pegar top N partidos
        df = df_partido.head(top_n).copy()
        
        # Criar figura com subplots
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        # Gráfico 1: Total gasto por partido
        ax1 = axes[0]
        bars1 = ax1.barh(df['partido'], df['total_gasto'] / 1_000_000, color=self.colors)
        ax1.set_xlabel('Total Gasto (Milhões R$)', fontsize=12)
        ax1.set_ylabel('Partido', fontsize=12)
        ax1.set_title(f'Total de Gastos por Partido (Top {top_n})', fontsize=14, fontweight='bold')
        ax1.invert_yaxis()
        
        # Adicionar valores nas barras
        for i, (idx, row) in enumerate(df.iterrows()):
            ax1.text(row['total_gasto'] / 1_000_000 + 0.1, i, 
                    f'R$ {row["total_gasto"]/1_000_000:.2f}M',
                    va='center', fontsize=9)
        
        # Gráfico 2: Média por deputado
        ax2 = axes[1]
        bars2 = ax2.barh(df['partido'], df['media_por_deputado'] / 1_000, color=self.colors)
        ax2.set_xlabel('Média por Deputado (Mil R$)', fontsize=12)
        ax2.set_ylabel('Partido', fontsize=12)
        ax2.set_title(f'Média de Gasto por Deputado (Top {top_n})', fontsize=14, fontweight='bold')
        ax2.invert_yaxis()
        
        # Adicionar valores nas barras
        for i, (idx, row) in enumerate(df.iterrows()):
            ax2.text(row['media_por_deputado'] / 1_000 + 1, i, 
                    f'R$ {row["media_por_deputado"]/1_000:.1f}K',
                    va='center', fontsize=9)
        
        plt.tight_layout()
        
        # Salvar
        filename = self.output_dir / 'gastos_por_partido.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✅ Salvo: {filename}")
        
        plt.close()
    
    def plot_gastos_estado(self, df_estado: pd.DataFrame, top_n: int = 15) -> None:
        """
        Gera gráfico de gastos por estado
        
        Args:
            df_estado: DataFrame com análise por estado
            top_n: Número de estados a exibir
        """
        print(f"\n📊 Gerando gráfico: Gastos por Estado (Top {top_n})...")
        
        # Pegar top N estados
        df = df_estado.head(top_n).copy()
        
        # Criar figura com subplots
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        # Gráfico 1: Total gasto por estado
        ax1 = axes[0]
        bars1 = ax1.barh(df['uf'], df['total_gasto'] / 1_000_000, color=self.colors)
        ax1.set_xlabel('Total Gasto (Milhões R$)', fontsize=12)
        ax1.set_ylabel('Estado (UF)', fontsize=12)
        ax1.set_title(f'Total de Gastos por Estado (Top {top_n})', fontsize=14, fontweight='bold')
        ax1.invert_yaxis()
        
        # Adicionar valores
        for i, (idx, row) in enumerate(df.iterrows()):
            ax1.text(row['total_gasto'] / 1_000_000 + 0.2, i, 
                    f'R$ {row["total_gasto"]/1_000_000:.2f}M',
                    va='center', fontsize=9)
        
        # Gráfico 2: Média por deputado
        ax2 = axes[1]
        bars2 = ax2.barh(df['uf'], df['media_por_deputado'] / 1_000, color=self.colors)
        ax2.set_xlabel('Média por Deputado (Mil R$)', fontsize=12)
        ax2.set_ylabel('Estado (UF)', fontsize=12)
        ax2.set_title(f'Média de Gasto por Deputado (Top {top_n})', fontsize=14, fontweight='bold')
        ax2.invert_yaxis()
        
        # Adicionar valores
        for i, (idx, row) in enumerate(df.iterrows()):
            ax2.text(row['media_por_deputado'] / 1_000 + 1, i, 
                    f'R$ {row["media_por_deputado"]/1_000:.1f}K',
                    va='center', fontsize=9)
        
        plt.tight_layout()
        
        # Salvar
        filename = self.output_dir / 'gastos_por_estado.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✅ Salvo: {filename}")
        
        plt.close()
    
    def plot_tipos_despesa(self, df_despesa: pd.DataFrame, top_n: int = 10) -> None:
        """
        Gera gráfico de tipos de despesa
        
        Args:
            df_despesa: DataFrame com análise por tipo de despesa
            top_n: Número de tipos a exibir
        """
        print(f"\n📊 Gerando gráfico: Tipos de Despesa (Top {top_n})...")
        
        # Pegar top N tipos
        df = df_despesa.head(top_n).copy()
        
        # Criar figura
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Gráfico de barras
        bars = ax.barh(range(len(df)), df['total_gasto'] / 1_000_000, color=self.colors[:len(df)])
        
        # Configurar eixos
        ax.set_yticks(range(len(df)))
        ax.set_yticklabels(df['tipo_despesa'], fontsize=10)
        ax.set_xlabel('Total Gasto (Milhões R$)', fontsize=12)
        ax.set_title(f'Top {top_n} Tipos de Despesa Mais Comuns', fontsize=14, fontweight='bold')
        ax.invert_yaxis()
        
        # Adicionar valores e percentuais
        for i, (idx, row) in enumerate(df.iterrows()):
            ax.text(row['total_gasto'] / 1_000_000 + 0.2, i, 
                    f'R$ {row["total_gasto"]/1_000_000:.2f}M ({row["percentual"]:.1f}%)',
                    va='center', fontsize=9)
        
        plt.tight_layout()
        
        # Salvar
        filename = self.output_dir / 'tipos_despesa.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✅ Salvo: {filename}")
        
        plt.close()
    
    def plot_top_deputados(self, df_deputados: pd.DataFrame, top_n: int = 15) -> None:
        """
        Gera gráfico dos deputados com maiores gastos
        
        Args:
            df_deputados: DataFrame com top deputados
            top_n: Número de deputados a exibir
        """
        print(f"\n📊 Gerando gráfico: Top {top_n} Deputados...")
        
        # Pegar top N
        df = df_deputados.head(top_n).copy()
        
        # Criar labels com nome, partido e UF
        df['label'] = df['nome_deputado'] + '\n(' + df['partido'] + '-' + df['uf'] + ')'
        
        # Criar figura
        fig, ax = plt.subplots(figsize=(14, 10))
        
        # Gráfico de barras
        bars = ax.barh(range(len(df)), df['total_gasto'] / 1_000, color=self.colors[:len(df)])
        
        # Configurar eixos
        ax.set_yticks(range(len(df)))
        ax.set_yticklabels(df['label'], fontsize=9)
        ax.set_xlabel('Total Gasto (Mil R$)', fontsize=12)
        ax.set_title(f'Top {top_n} Deputados com Maiores Gastos', fontsize=14, fontweight='bold')
        ax.invert_yaxis()
        
        # Adicionar valores
        for i, (idx, row) in enumerate(df.iterrows()):
            ax.text(row['total_gasto'] / 1_000 + 2, i, 
                    f'R$ {row["total_gasto"]/1_000:.1f}K',
                    va='center', fontsize=9)
        
        plt.tight_layout()
        
        # Salvar
        filename = self.output_dir / 'top_deputados.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✅ Salvo: {filename}")
        
        plt.close()
    
    def plot_resumo_geral(self, df_partido: pd.DataFrame, df_estado: pd.DataFrame) -> None:
        """
        Gera gráfico de resumo geral
        
        Args:
            df_partido: DataFrame com análise por partido
            df_estado: DataFrame com análise por estado
        """
        print("\n📊 Gerando gráfico: Resumo Geral...")
        
        # Criar figura com subplots
        fig = plt.figure(figsize=(16, 10))
        gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
        
        # 1. Top 10 Partidos (total)
        ax1 = fig.add_subplot(gs[0, 0])
        df_p = df_partido.head(10)
        ax1.bar(df_p['partido'], df_p['total_gasto'] / 1_000_000, color=self.colors[:10])
        ax1.set_xlabel('Partido', fontsize=10)
        ax1.set_ylabel('Total Gasto (Milhões R$)', fontsize=10)
        ax1.set_title('Top 10 Partidos - Total de Gastos', fontsize=12, fontweight='bold')
        ax1.tick_params(axis='x', rotation=45)
        
        # 2. Top 10 Estados (total)
        ax2 = fig.add_subplot(gs[0, 1])
        df_e = df_estado.head(10)
        ax2.bar(df_e['uf'], df_e['total_gasto'] / 1_000_000, color=self.colors[:10])
        ax2.set_xlabel('Estado (UF)', fontsize=10)
        ax2.set_ylabel('Total Gasto (Milhões R$)', fontsize=10)
        ax2.set_title('Top 10 Estados - Total de Gastos', fontsize=12, fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        
        # 3. Top 10 Partidos (média por deputado)
        ax3 = fig.add_subplot(gs[1, 0])
        df_p_sorted = df_partido.sort_values('media_por_deputado', ascending=False).head(10)
        ax3.bar(df_p_sorted['partido'], df_p_sorted['media_por_deputado'] / 1_000, color=self.colors[:10])
        ax3.set_xlabel('Partido', fontsize=10)
        ax3.set_ylabel('Média por Deputado (Mil R$)', fontsize=10)
        ax3.set_title('Top 10 Partidos - Média por Deputado', fontsize=12, fontweight='bold')
        ax3.tick_params(axis='x', rotation=45)
        
        # 4. Top 10 Estados (média por deputado)
        ax4 = fig.add_subplot(gs[1, 1])
        df_e_sorted = df_estado.sort_values('media_por_deputado', ascending=False).head(10)
        ax4.bar(df_e_sorted['uf'], df_e_sorted['media_por_deputado'] / 1_000, color=self.colors[:10])
        ax4.set_xlabel('Estado (UF)', fontsize=10)
        ax4.set_ylabel('Média por Deputado (Mil R$)', fontsize=10)
        ax4.set_title('Top 10 Estados - Média por Deputado', fontsize=12, fontweight='bold')
        ax4.tick_params(axis='x', rotation=45)
        
        plt.suptitle('Resumo Geral de Gastos Parlamentares', fontsize=16, fontweight='bold', y=0.995)
        
        # Salvar
        filename = self.output_dir / 'resumo_geral.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"✅ Salvo: {filename}")
        
        plt.close()
    
    def gerar_todos_graficos(self, relatorio: dict) -> None:
        """
        Gera todos os gráficos do relatório
        
        Args:
            relatorio: Dicionário com todos os DataFrames de análise
        """
        print("\n" + "=" * 70)
        print("📊 GERANDO VISUALIZAÇÕES")
        print("=" * 70)
        
        self.plot_gastos_partido(relatorio['por_partido'])
        self.plot_gastos_estado(relatorio['por_estado'])
        self.plot_tipos_despesa(relatorio['por_tipo_despesa'])
        self.plot_top_deputados(relatorio['top_deputados'])
        self.plot_resumo_geral(relatorio['por_partido'], relatorio['por_estado'])
        
        print("\n" + "=" * 70)
        print(f"✅ TODAS AS VISUALIZAÇÕES SALVAS EM: {self.output_dir}/")
        print("=" * 70)


if __name__ == '__main__':
    print("Este módulo deve ser importado, não executado diretamente.")
    print("Use: from visualizer import Visualizer")
