# 📥 Script para Download Automático dos Dados

## Baixar Ano 2023 (Recomendado)

```powershell
# Navegar até a pasta de dados
cd "c:\Users\thale\Docs\Faculdade\Ciencia de dados\Analise de dados do governo api\dados"

# Baixar arquivo (pode demorar alguns minutos - arquivo ~180 MB)
Invoke-WebRequest -Uri "https://www.camara.leg.br/cota-parlamentar/dados/dataset/Ano-2023.csv" -OutFile "Ano-2023.csv"
```

## Baixar Outros Anos

### Ano 2024
```powershell
Invoke-WebRequest -Uri "https://www.camara.leg.br/cota-parlamentar/dados/dataset/Ano-2024.csv" -OutFile "Ano-2024.csv"
```

### Ano 2022
```powershell
Invoke-WebRequest -Uri "https://www.camara.leg.br/cota-parlamentar/dados/dataset/Ano-2022.csv" -OutFile "Ano-2022.csv"
```

### Ano 2021
```powershell
Invoke-WebRequest -Uri "https://www.camara.leg.br/cota-parlamentar/dados/dataset/Ano-2021.csv" -OutFile "Ano-2021.csv"
```

## Verificar Download

```powershell
# Ver tamanho do arquivo
Get-Item Ano-2023.csv | Select-Object Name, Length

# Ver primeiras linhas
Get-Content Ano-2023.csv -Head 5
```

## Em Caso de Erro

Se o download falhar, baixe manualmente:
1. Abra: https://www.camara.leg.br/cota-parlamentar/
2. Clique em "Arquivos de Dados"
3. Baixe o arquivo desejado
4. Mova para a pasta `dados/`
