"""
Script Principal - Análise Comparativa de Gastos da Cota Parlamentar

Este script coordena todo o processo de análise:
1. Carrega e limpa dados do CSV
2. Busca dados cadastrais na API
3. Cruza os dados
4. Gera análises
5. Cria visualizações
6. Salva resultados
7. Gera apresentação PowerPoint

Uso:
    python main.py <caminho_para_csv>
    
Exemplo:
    python main.py dados/Ano-2023.csv
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Importar módulos do projeto
from api_client import CamaraAPI
from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from visualizer import Visualizer
from gerar_apresentacao_completa import ApresentacaoAnalise


def print_header():
    """Exibe cabeçalho do programa"""
    print("\n" + "=" * 80)
    print("  ANÁLISE COMPARATIVA DE GASTOS DA COTA PARLAMENTAR")
    print("  Câmara dos Deputados - Brasil")
    print("=" * 80)
    print(f"  Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 80 + "\n")


def salvar_resultados(relatorio: dict, output_dir: str = 'resultados'):
    """
    Salva os resultados das análises em arquivos CSV
    
    Args:
        relatorio: Dicionário com DataFrames das análises
        output_dir: Diretório de saída
    """
    print("\n" + "=" * 70)
    print("💾 SALVANDO RESULTADOS")
    
    # Criar pasta com timestamp para esta execução
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    execution_dir = Path(output_dir) / f'execucao_{timestamp}'
    execution_dir.mkdir(parents=True, exist_ok=True)
    print(f"📁 Pasta de execução: {execution_dir}")
    print("=" * 70)
    
    # Salvar cada análise
    arquivos_salvos = []
    
    # 1. Dados cruzados completos
    filename = execution_dir / 'analise_completa.csv'
    relatorio['dados_cruzados'].to_csv(filename, index=False, encoding='utf-8-sig')
    arquivos_salvos.append(filename)
    print(f"✅ {filename}")
    
    # 2. Análise por partido
    filename = execution_dir / 'gastos_por_partido.csv'
    relatorio['por_partido'].to_csv(filename, index=False, encoding='utf-8-sig')
    arquivos_salvos.append(filename)
    print(f"✅ {filename}")
    
    # 3. Análise por estado
    filename = execution_dir / 'gastos_por_estado.csv'
    relatorio['por_estado'].to_csv(filename, index=False, encoding='utf-8-sig')
    arquivos_salvos.append(filename)
    print(f"✅ {filename}")
    
    # 4. Análise por tipo de despesa
    filename = execution_dir / 'gastos_por_tipo_despesa.csv'
    relatorio['por_tipo_despesa'].to_csv(filename, index=False, encoding='utf-8-sig')
    arquivos_salvos.append(filename)
    print(f"✅ {filename}")
    
    # 5. Top deputados
    filename = execution_dir / 'top_deputados.csv'
    relatorio['top_deputados'].to_csv(filename, index=False, encoding='utf-8-sig')
    arquivos_salvos.append(filename)
    print(f"✅ {filename}")
    
    print("\n" + "=" * 70)
    print(f"✅ {len(arquivos_salvos)} ARQUIVOS SALVOS EM: {execution_dir}/")
    print("=" * 70)
    
    return arquivos_salvos, execution_dir


def exibir_resumo_final(relatorio: dict):
    """
    Exibe resumo final das principais descobertas
    
    Args:
        relatorio: Dicionário com DataFrames das análises
    """
    print("\n" + "=" * 80)
    print("  📊 RESUMO FINAL - PRINCIPAIS DESCOBERTAS")
    print("=" * 80)
    
    # Estatísticas gerais
    df_cruzado = relatorio['dados_cruzados']
    df_cruzado_limpo = df_cruzado[df_cruzado['partido'] != 'NÃO IDENTIFICADO']
    
    total_gasto = df_cruzado_limpo['valor'].sum()
    num_deputados = df_cruzado_limpo['nome_deputado'].nunique()
    num_registros = len(df_cruzado_limpo)
    
    print(f"\n💰 VALORES TOTAIS:")
    print(f"   Total gasto no período: R$ {total_gasto:,.2f}")
    print(f"   Número de deputados: {num_deputados}")
    print(f"   Número de registros: {num_registros:,}")
    print(f"   Gasto médio por deputado: R$ {total_gasto/num_deputados:,.2f}")
    
    # Top 3 partidos
    df_partido = relatorio['por_partido']
    print(f"\n🏆 TOP 3 PARTIDOS (Total de Gastos):")
    for i, row in df_partido.head(3).iterrows():
        print(f"   {i+1}. {row['partido']}: R$ {row['total_gasto']:,.2f}")
        print(f"      → Média por deputado: R$ {row['media_por_deputado']:,.2f}")
        print(f"      → Número de deputados: {int(row['num_deputados'])}")
    
    # Top 3 estados
    df_estado = relatorio['por_estado']
    print(f"\n🏆 TOP 3 ESTADOS (Total de Gastos):")
    for i, row in df_estado.head(3).iterrows():
        print(f"   {i+1}. {row['uf']}: R$ {row['total_gasto']:,.2f}")
        print(f"      → Média por deputado: R$ {row['media_por_deputado']:,.2f}")
        print(f"      → Número de deputados: {int(row['num_deputados'])}")
    
    # Top 3 tipos de despesa
    df_despesa = relatorio['por_tipo_despesa']
    print(f"\n🏆 TOP 3 TIPOS DE DESPESA:")
    for i, row in df_despesa.head(3).iterrows():
        print(f"   {i+1}. {row['tipo_despesa']}")
        print(f"      → Total: R$ {row['total_gasto']:,.2f} ({row['percentual']:.1f}%)")
    
    # Top 3 deputados
    df_deputados = relatorio['top_deputados']
    print(f"\n🏆 TOP 3 DEPUTADOS (Maiores Gastos):")
    for i, row in df_deputados.head(3).iterrows():
        print(f"   {i+1}. {row['nome_deputado']} ({row['partido']}-{row['uf']})")
        print(f"      → Total gasto: R$ {row['total_gasto']:,.2f}")
    
    print("\n" + "=" * 80)


def gerar_apresentacao(execution_dir: Path):
    """
    Gera apresentação PowerPoint dentro da pasta de execução
    
    Args:
        execution_dir: Pasta da execução atual
    """
    try:
        print("\n📌 Gerando apresentação PowerPoint completa...")
        
        # Definir caminho de saída
        output_file = execution_dir / "Apresentacao_Completa.pptx"
        
        # Gerar apresentação
        apresentacao = ApresentacaoAnalise(execution_dir, output_path=output_file)
        apresentacao.gerar()
        
        print(f"✅ Apresentação salva: {output_file.name}")
        
        return True
        
    except Exception as e:
        print(f"⚠️  Aviso: Não foi possível gerar a apresentação: {e}")
        print("   A análise foi concluída com sucesso.")
        return False


def main():
    """Função principal do programa"""
    
    # Configurar argumentos da linha de comando
    parser = argparse.ArgumentParser(
        description='Análise Comparativa de Gastos da Cota Parlamentar',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos de uso:
  python main.py dados/Ano-2023.csv
  python main.py "C:/Downloads/Ano-2023.csv"
  
Para baixar os dados:
  https://www.camara.leg.br/cota-parlamentar/
        '''
    )
    
    parser.add_argument(
        'csv_path',
        help='Caminho para o arquivo CSV de despesas'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='resultados',
        help='Diretório para salvar os resultados (padrão: resultados)'
    )
    
    # Parse dos argumentos
    args = parser.parse_args()
    
    # Exibir cabeçalho
    print_header()
    
    try:
        # ETAPA 1: Carregar e limpar dados do CSV
        print("📋 ETAPA 1/5: Carregando dados do CSV")
        print("-" * 70)
        loader = DataLoader(args.csv_path)
        loader.carregar_csv()
        df_despesas = loader.limpar_dados()
        loader.exibir_resumo()
        
        # ETAPA 2: Buscar dados cadastrais na API
        print("\n📋 ETAPA 2/5: Buscando dados cadastrais na API")
        print("-" * 70)
        api = CamaraAPI()
        df_deputados = api.buscar_deputados()
        
        # ETAPA 3: Analisar e cruzar dados
        print("\n📋 ETAPA 3/5: Analisando e cruzando dados")
        print("-" * 70)
        analyzer = DataAnalyzer(df_despesas, df_deputados)
        relatorio = analyzer.gerar_relatorio_completo()
        
        # ETAPA 4: Salvar resultados
        print("\n📋 ETAPA 4/5: Salvando resultados")
        print("-" * 70)
        arquivos, execution_dir = salvar_resultados(relatorio, output_dir=args.output)
        
        # ETAPA 5: Gerar visualizações
        print("\n📋 ETAPA 5/6: Gerando visualizações")
        print("-" * 70)
        visualizer = Visualizer(output_dir=str(execution_dir))
        visualizer.gerar_todos_graficos(relatorio)
        
        # ETAPA 6: Gerar apresentação PowerPoint
        print("\n📋 ETAPA 6/6: Gerando apresentação")
        print("-" * 70)
        gerar_apresentacao(execution_dir)
        
        # Exibir resumo final
        exibir_resumo_final(relatorio)
        
        # Mensagem de sucesso
        print("\n" + "=" * 80)
        print("  ✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
        print("=" * 80)
        print(f"\n  📁 Resultados salvos em: {execution_dir.absolute()}/")
        print(f"  📊 {len(arquivos)} arquivos CSV gerados")
        print(f"  📈 5 gráficos gerados (formato PNG)")
        print(f"  📑 1 apresentação PowerPoint gerada")
        print("\n" + "=" * 80 + "\n")
        
    except FileNotFoundError as e:
        print(f"\n❌ ERRO: {e}")
        print("\n💡 Dica: Baixe o arquivo CSV em:")
        print("   https://www.camara.leg.br/cota-parlamentar/\n")
        sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Análise interrompida pelo usuário.\n")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")
        print("\n💡 Verifique:")
        print("   - Conexão com a internet (para acessar a API)")
        print("   - Formato do arquivo CSV")
        print("   - Permissões de escrita na pasta de saída\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
