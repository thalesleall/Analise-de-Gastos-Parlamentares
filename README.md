# 📊 Análise de Gastos Parlamentares

> Análise comparativa de gastos da Cota Parlamentar por Partido e Estado - Câmara dos Deputados

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📖 Sobre o Projeto

Sistema automatizado de análise de dados governamentais que cruza informações de despesas parlamentares (CSV) com dados cadastrais da API da Câmara dos Deputados, gerando análises estatísticas e visualizações sobre gastos por partido, estado e tipo de despesa.

### 🎯 Objetivos

- Identificar padrões de gastos por partido político
- Comparar despesas entre estados brasileiros
- Analisar tipos de despesas mais comuns
- Rankear deputados com maiores gastos
- Automatizar análise exploratória de dados governamentais

## ✨ Funcionalidades

- ✅ **Carregamento inteligente** de CSV com validação e limpeza de dados
- ✅ **Integração com API** da Câmara dos Deputados
- ✅ **Cruzamento de dados** via normalização de nomes (>95% taxa de identificação)
- ✅ **Análises estatísticas** agregadas por múltiplas dimensões
- ✅ **Visualizações profissionais** em alta resolução (300 DPI)
- ✅ **Organização automática** de resultados por execução com timestamp
- ✅ **Exportação completa** em CSV e PNG

## 🚀 Como Usar

### 📋 Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### 🔧 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/thalesleall/analise-gastos-parlamentares.git
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

### 📥 Obtenha os Dados

Baixe o CSV de despesas parlamentares em:
- [Portal de Dados Abertos da Câmara](https://www.camara.leg.br/cota-parlamentar/)

Salve o arquivo na pasta `dados/` com o nome `Ano-YYYY.csv` (exemplo: `Ano-2025.csv`)

### ▶️ Execute a Análise

```bash
python src/main.py dados/Ano-2025.csv
```

**Parâmetros opcionais:**
```bash
python src/main.py dados/Ano-2025.csv --output resultados
```

**O que acontece automaticamente:**
1. ✅ Carrega e limpa os dados do CSV
2. ✅ Busca informações dos deputados na API
3. ✅ Cruza e analisa os dados
4. ✅ Salva 5 arquivos CSV com resultados
5. ✅ Gera 5 gráficos profissionais (PNG 300 DPI)
6. ✅ **Cria apresentação PowerPoint completa (15 slides)**

### 📊 Resultados

Os resultados são salvos automaticamente em `resultados/execucao_YYYYMMDD_HHMMSS/`:

**5 arquivos CSV:**
- `analise_completa.csv` - Dados completos do cruzamento
- `gastos_por_partido.csv` - Agregação por partido
- `gastos_por_estado.csv` - Agregação por estado (UF)
- `gastos_por_tipo_despesa.csv` - Tipos de despesa principais
- `top_deputados.csv` - Top 20 deputados com maiores gastos

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

## 📁 Estrutura do Projeto

```
📦 analise-gastos-parlamentares/
├── 📂 dados/                    # Arquivos CSV de entrada
│   └── Ano-2025.csv
├── 📂 src/                      # Código fonte
│   ├── api_client.py           # Cliente API da Câmara
│   ├── data_loader.py          # Carregamento e limpeza de dados
│   ├── data_analyzer.py        # Análise e cruzamento de dados
│   ├── visualizer.py           # Geração de gráficos
│   └── main.py                 # Script principal
├── 📂 resultados/               # Outputs organizados por execução
│   ├── execucao_20251020_212403/
│   │   ├── *.csv               # 5 arquivos de análise
│   │   └── *.png               # 5 gráficos
│   └── README.md
├── 📄 COMO_FUNCIONA.md          # Documentação técnica resumida
├── 📄 README.md                 # Este arquivo
└── 📄 requirements.txt          # Dependências Python
```

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.13 | Linguagem base |
| Pandas | 2.3.3 | Manipulação de dados |
| NumPy | 2.3.4 | Operações numéricas |
| Matplotlib | 3.10.7 | Visualizações base |
| Seaborn | 0.13.2 | Visualizações avançadas |
| Requests | 2.32.5 | Chamadas API REST |
| Unidecode | 1.4.0 | Normalização de texto |

## 📚 Fontes de Dados

### 1. CSV de Despesas
- **Fonte:** Portal de Dados Abertos da Câmara dos Deputados
- **URL:** https://www.camara.leg.br/cota-parlamentar/
- **Formato:** CSV com ~285.000 registros
- **Campos principais:** txNomeParlamentar, vlrLiquido, txtDescricao

### 2. API Cadastral
- **Fonte:** API REST da Câmara dos Deputados
- **URL:** https://dadosabertos.camara.leg.br/api/v2/deputados
- **Formato:** JSON
- **Dados:** nome, siglaPartido, siglaUf

## 👥 Equipe

- **Leticia Cristina Silva** - 21352
- **Gabriel Davi Lopes Jacobini** - 24734
- **Thales Vinicius Leal Barcelos** - 24740
- **Maria Fernanda Leite Felicíssimo** - 24767

**Disciplina:** Ciência de Dados - 2025

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

## 📞 Contato

Para dúvidas ou sugestões, abra uma [Issue](https://github.com/thalesleall/analise-gastos-parlamentares/issues) no GitHub.

---

<div align="center">
  
**Desenvolvido com 💙 para transparência dos dados públicos brasileiros**

</div>
