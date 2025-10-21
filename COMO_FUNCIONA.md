# 🔧 Como Funciona

## 📋 Visão Geral

Este projeto analisa gastos parlamentares cruzando dados de despesas (CSV) com informações cadastrais da API da Câmara dos Deputados.

## 🔄 Fluxo de Execução

```
1. Carrega CSV de despesas → Limpa dados (nulos, valores inválidos)
2. Busca deputados na API → Obtém partido e estado
3. Cruza dados por nome → Padroniza (uppercase + remove acentos)
4. Gera análises → Por partido, estado, tipo de despesa, top deputados
5. Cria visualizações → 5 gráficos em PNG (300 DPI)
6. Salva resultados → CSV + PNG em pasta timestampada
7. Gera apresentação → PowerPoint completo (15 slides) automaticamente
```

## 📦 Estrutura Modular

**`src/api_client.py`**
- Conecta à API da Câmara
- Retorna DataFrame com: nome, partido, UF

**`src/data_loader.py`**
- Carrega e limpa CSV
- Remove nulos e valores ≤ 0
- Padroniza nomes (uppercase, sem acentos)

**`src/data_analyzer.py`**
- Cruza CSV + API por nome
- Gera agregações (partido, estado, tipo despesa)
- Identifica top 20 deputados

**`src/visualizer.py`**
- Cria 5 gráficos profissionais
- Formato PNG 300 DPI
- Estilos com matplotlib/seaborn

**`src/main.py`**
- Orquestra todo o processo
- Exibe progresso em tempo real
- Salva em pasta `execucao_TIMESTAMP/`

## 🎯 Outputs

Cada execução gera em `resultados/execucao_YYYYMMDD_HHMMSS/`:

**CSV:**
- `analise_completa.csv` - Dados completos cruzados
- `gastos_por_partido.csv` - Agregação por partido
- `gastos_por_estado.csv` - Agregação por estado
- `gastos_por_tipo_despesa.csv` - Principais despesas
- `top_deputados.csv` - Top 20 maiores gastos

**PNG:**
- `gastos_por_partido.png` - Gráfico barras por partido
- `gastos_por_estado.png` - Gráfico barras por estado
- `tipos_despesa.png` - Principais tipos de despesa
- `top_deputados.png` - Top 20 deputados
- `resumo_geral.png` - Dashboard 4 em 1

**PowerPoint:**
- `Apresentacao_Completa.pptx` - Apresentação completa (15 slides)
  - Gerada automaticamente ao final da análise
  - Inclui todos os gráficos e insights
  - Pronta para apresentação

## ⚙️ Tecnologias

- **Python 3.13** - Linguagem base
- **Pandas** - Manipulação de dados
- **Requests** - Chamadas API
- **Matplotlib/Seaborn** - Visualizações
- **Unidecode** - Normalização de texto

## 📊 Dados

**Entrada:** CSV de despesas da Câmara (~285k registros)
**API:** https://dadosabertos.camara.leg.br/api/v2/deputados
**Taxa de identificação:** >95% dos deputados
