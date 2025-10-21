# 📊 Resultados das Análises

Esta pasta armazena os resultados de cada execução do programa de análise.

## 📁 Estrutura

Cada execução cria uma pasta com timestamp: `execucao_YYYYMMDD_HHMMSS/`

### Conteúdo de cada execução:

**Arquivos CSV:**
- `analise_completa.csv` - Dados completos do cruzamento CSV + API
- `gastos_por_partido.csv` - Agregação por partido político
- `gastos_por_estado.csv` - Agregação por estado (UF)
- `gastos_por_tipo_despesa.csv` - Agregação por tipo de despesa
- `top_deputados.csv` - Top 20 deputados com maiores gastos

**Gráficos PNG (300 DPI):**
- `gastos_por_partido.png` - Gráfico de barras: gastos por partido
- `gastos_por_estado.png` - Gráfico de barras: gastos por estado
- `tipos_despesa.png` - Gráfico de barras: principais tipos de despesa
- `top_deputados.png` - Gráfico de barras: top 20 deputados
- `resumo_geral.png` - Dashboard com 4 gráficos principais

## 🔍 Como visualizar

1. Navegue até a pasta da execução desejada
2. Abra os arquivos CSV em Excel/LibreOffice ou Python/Pandas
3. Visualize os gráficos PNG em qualquer visualizador de imagens
