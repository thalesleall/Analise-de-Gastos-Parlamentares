# 📊 Análise de Gastos Parlamentares

> Sistema inteligente de análise de gastos da Câmara dos Deputados

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)

## 📖 O Que Faz

Analisa automaticamente os gastos parlamentares cruzando dados de despesas com informações da API da Câmara dos Deputados. Gera relatórios, gráficos e apresentação PowerPoint completa em poucos minutos.

### 🎯 Análises Incluídas

- 📊 Gastos por partido político
- 🗺️ Gastos por estado (UF)
- 💳 Principais tipos de despesa
- 👥 Ranking dos deputados
- 📈 Dashboard visual completo

## 🚀 Como Usar

### 📋 Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### 🔧 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/thalesleall/Analise-de-Gastos-Parlamentares.git
cd analise-gastos-parlamentares
```

2. **Crie e ative o ambiente virtual**

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### 📥 Dados

Baixe o CSV em: [Portal da Câmara](https://www.camara.leg.br/cota-parlamentar/)
Salve na pasta `dados/` como `Ano-2025.csv`

### ▶️ Executar

```bash
python src/main.py dados/Ano-2025.csv
```

### 📊 Resultados (em `resultados/execucao_TIMESTAMP/`)

**5 CSVs + 5 Gráficos + 1 PowerPoint:**
- `analise_completa.csv` - Dados completos
- `gastos_por_partido.csv` - Por partido
- `gastos_por_estado.csv` - Por estado
- `gastos_por_tipo_despesa.csv` - Tipos de despesa
- `top_deputados.csv` - Top 20 deputados
- 5 gráficos PNG profissionais (300 DPI)
- `Apresentacao_Completa.pptx` (15 slides)

**5 gráficos PNG (300 DPI):**
- `gastos_por_partido.png` - Gastos totais por partido
- `gastos_por_estado.png` - Gastos totais por estado
- `tipos_despesa.png` - Principais tipos de despesa
- `top_deputados.png` - Top 20 deputados
- `resumo_geral.png` - Dashboard com 4 análises principais

**1 apresentação PowerPoint (15 slides):**
- `Apresentacao_Completa.pptx` - Apresentação completa com:
  - Título e integrantes
  - Metodologia e tecnologias
  - Todos os gráficos gerados
  - Insights e resultados quantitativos
  - Tabela dos top 5 partidos
  - Conclusão e agradecimentos

### 📑 Gerar Apresentação Manualmente (Opcional)

Se quiser gerar apenas a apresentação sem executar a análise novamente:

```bash
python gerar_apresentacao_completa.py
# Usa automaticamente a execução mais recente
```

## 📁 Estrutura

```
📦 projeto/
├── 📂 dados/           # CSV de entrada
├── 📂 src/             # Código Python (5 módulos)
├── 📂 scripts/         # Script de apresentação
├── 📂 resultados/      # Saídas por execução
└── 📄 requirements.txt
```

## 🛠️ Tecnologias

- **Python 3.13** + Pandas + Matplotlib + Seaborn
- **API:** Câmara dos Deputados (REST)
- **Bibliotecas:** requests, unidecode, python-pptx

## 📚 Dados

- **CSV:** [Portal da Câmara](https://www.camara.leg.br/cota-parlamentar/) (~285k registros)
- **API:** https://dadosabertos.camara.leg.br/api/v2/deputados

## 🎓 Equipe

**Grupo 1 - Ciência de Dados (2025)**

- Leticia (21352)
- Gabriel (24734)
- Thales (24740)
- Maria Fernanda (24767)

---

� **Análise de Dados Governamentais - Câmara dos Deputados**
