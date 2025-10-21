# 🛠️ Scripts Auxiliares

Esta pasta contém scripts auxiliares para geração de documentação.

## 📄 Scripts Disponíveis

### `gerar_powerpoint.py`
Gera apresentação PowerPoint com os resultados da análise.

**Uso:**
```bash
python scripts/gerar_powerpoint.py
```

**Output:** `Apresentacao_Analise_Gastos_Parlamentares.pptx` (9 slides)

---

### `gerar_word.py`
Gera documento Word com apresentação detalhada das fontes de dados.

**Uso:**
```bash
python scripts/gerar_word.py
```

**Output:** `Apresentacao_Fontes_Dados.docx` (~10-12 páginas)

---

### `atualizar_powerpoint.py`
Atualiza PowerPoint existente adicionando slide com integrantes do grupo.

**Uso:**
```bash
python scripts/atualizar_powerpoint.py
```

**Output:** Atualiza `Apresentacao_Analise_Gastos_Parlamentares.pptx`

---

## 📦 Script Principal (Raiz do Projeto)

### `../gerar_apresentacao_completa.py`
**NOVO!** Gera apresentação PowerPoint completa explicando todo o projeto.

**Uso:**
```bash
python gerar_apresentacao_completa.py
# ou especificar pasta de resultados
python gerar_apresentacao_completa.py resultados/execucao_20251020_212403
```

**Output:** `Apresentacao_Completa_Analise.pptx` (15 slides)

**Conteúdo:**
1. Título do projeto
2. Integrantes do grupo
3. O que foi feito
4. Metodologia aplicada
5. Tecnologias utilizadas
6-10. Gráficos da análise (5 slides)
11. Principais insights
12. Resultados quantitativos
13. Top 5 partidos (tabela)
14. Conclusão
15. Agradecimentos

---

## 📦 Dependências

Estes scripts requerem as bibliotecas:
- `python-pptx` - Manipulação de PowerPoint
- `python-docx` - Manipulação de Word
- `pandas` - Leitura de dados

Instalação:
```bash
pip install python-pptx python-docx pandas
```

## ⚠️ Importante

Os scripts de PowerPoint e Word esperam que a análise já tenha sido executada e que existam resultados em `resultados/execucao_*/`.
