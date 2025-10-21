# 📊 Análise de Gastos Parlamentares - Estrutura Final

## 📁 Estrutura do Projeto

```
analise-gastos-parlamentares/
│
├── 📂 dados/                           # Dados de entrada (CSVs)
│   ├── .gitkeep
│   └── Ano-2025.csv                    # Adicione seus CSVs aqui
│
├── 📂 src/                             # Código fonte principal
│   ├── api_client.py                   # Cliente API da Câmara
│   ├── data_loader.py                  # Carregamento e limpeza
│   ├── data_analyzer.py                # Análise e cruzamento
│   ├── visualizer.py                   # Geração de gráficos
│   └── main.py                         # Script principal
│
├── 📂 resultados/                      # Outputs por execução
│   ├── README.md
│   └── execucao_YYYYMMDD_HHMMSS/      # Cada execução cria uma pasta
│       ├── *.csv                       # 5 arquivos de análise
│       └── *.png                       # 5 gráficos (300 DPI)
│
├── 📂 scripts/                         # Scripts auxiliares
│   ├── README.md
│   ├── gerar_powerpoint.py            # Gera apresentação PPT
│   ├── gerar_word.py                  # Gera documento Word
│   └── atualizar_powerpoint.py        # Atualiza PPT
│
├── 📂 venv/                            # Ambiente virtual Python
│
├── 📄 .gitignore                       # Arquivos ignorados pelo Git
├── 📄 COMO_FUNCIONA.md                 # Doc técnica resumida
├── 📄 README.md                        # Este arquivo
├── 📄 requirements.txt                 # Dependências Python
│
├── 📄 Apresentacao_Analise_Gastos_Parlamentares.pptx  # PowerPoint gerado
└── 📄 Apresentacao_Fontes_Dados.docx                  # Word gerado
```

## 🚀 Como Usar

### 1. Instalação

```bash
# Clone o repositório
git clone <url-do-repo>
cd analise-gastos-parlamentares

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt
```

### 2. Obtenha os Dados

Baixe o CSV em: https://www.camara.leg.br/cota-parlamentar/
Coloque em: `dados/Ano-YYYY.csv`

### 3. Execute a Análise

```bash
python src/main.py dados/Ano-2025.csv
```

### 4. Resultados

Os resultados são salvos em: `resultados/execucao_YYYYMMDD_HHMMSS/`

- **5 CSVs:** análises detalhadas
- **5 PNGs:** gráficos profissionais (300 DPI)

## 📊 Outputs

Cada execução gera:

### Arquivos CSV:
1. `analise_completa.csv` - Dados completos do cruzamento CSV + API
2. `gastos_por_partido.csv` - Agregação por partido político
3. `gastos_por_estado.csv` - Agregação por estado (UF)
4. `gastos_por_tipo_despesa.csv` - Principais tipos de despesa
5. `top_deputados.csv` - Top 20 deputados com maiores gastos

### Gráficos PNG (300 DPI):
1. `gastos_por_partido.png` - Barras: gastos por partido
2. `gastos_por_estado.png` - Barras: gastos por estado
3. `tipos_despesa.png` - Barras: tipos de despesa
4. `top_deputados.png` - Barras: top 20 deputados
5. `resumo_geral.png` - Dashboard 4 em 1

## 🛠️ Tecnologias

- **Python 3.13**
- **Pandas** - Manipulação de dados
- **NumPy** - Operações numéricas
- **Matplotlib/Seaborn** - Visualizações
- **Requests** - API REST
- **Unidecode** - Normalização de texto

## 📚 Documentação

- `README.md` - Guia completo do projeto
- `COMO_FUNCIONA.md` - Explicação técnica resumida
- `resultados/README.md` - Sobre a estrutura de resultados
- `scripts/README.md` - Scripts auxiliares

## 👥 Equipe

- Leticia Cristina Silva - 21352
- Gabriel Davi Lopes Jacobini - 24734
- Thales Vinicius Leal Barcelos - 24740
- Maria Fernanda Leite Felicíssimo - 24767

**Disciplina:** Ciência de Dados - 2025

---

✨ **Projeto reestruturado em 20/10/2025**
