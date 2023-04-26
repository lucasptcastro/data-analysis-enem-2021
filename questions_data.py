import pandas as pd
import matplotlib.pyplot as plt
from log.logger import Logger
from analises import Analises

classe_logger = Logger("ANALISE").get_logger()
classe_analises = Analises('./dados/MICRODADOS_ENEM_2021_FORMATADO.csv', limitador=10000)

microdados_enem = classe_analises.df
colunas_selecionadas = ['NU_INSCRICAO', 'NU_NOTA_MT', 'NU_NOTA_REDACAO',
 'Q001', 'Q002']
microdados_enem_selecionados = microdados_enem.filter(items=colunas_selecionadas)
microdados_enem_selecionados = microdados_enem_selecionados.dropna()

# Q01 => Até que série seu pai, ou o homem responsável por você, estudou?
# Q02 => Até que série sua mãe, ou a mulher responsável por você, estudou?
q001e002Dicionario = {
    "A": "Nunca estudou",
    "B": "Não completou a 4ªsérie/5°ano do Ensino Fundamental",
    "C": "Completou a 4ªsérie/5°ano, mas não completou a 8ªsérie/9°ano do Ensino Fundamental",
    "D": "Completou a 8ªsérie/9°ano do Ensino Fundamental, mas não completou o Ensino Médio.",
    "E": "Completou o Ensino Médio, mas não completou a Faculdade.",
    "F": "Completou a Faculdade, mas não completou a Pós-Graduação.",
    "G": "Completou a Pós-Graduação.",
    "H": "Não sei."            
}

# Colunas extras com a descrição dos valores das notas Q001 e Q002
microdados_enem_selecionados['NO_Q001'] = [q001e002Dicionario[resp] for resp in microdados_enem_selecionados.Q001]
microdados_enem_selecionados['NO_Q002'] = [q001e002Dicionario[resp] for resp in microdados_enem_selecionados.Q002]

# Mostra a contagem de dados socioeconômicos em relação a educação dos pais
print(microdados_enem_selecionados.filter(items=['NU_INSCRICAO', 'NO_Q001']).groupby('NO_Q001').count().sort_values(by='NU_INSCRICAO', ascending=False).head(10))

# Mostra a contagem de dados socioeconômicos em relação a educação das mães
print(microdados_enem_selecionados.filter(items=['NU_INSCRICAO', 'NO_Q002']).groupby('NO_Q002').count().sort_values(by='NU_INSCRICAO', ascending=False).head(10))

# Mostra a média de notas da redação em baseada na educação dos pais
print(microdados_enem_selecionados.filter(items=['NU_NOTA_REDACAO', 'NO_Q001']).groupby('NO_Q001').mean().sort_values(by="NU_NOTA_REDACAO", ascending=False).head(10))

# Mostra a média de notas da redação em baseada na educação das mães
print(microdados_enem_selecionados.filter(items=['NU_NOTA_REDACAO', 'NO_Q002']).groupby('NO_Q002').mean().sort_values(by="NU_NOTA_REDACAO", ascending=False).head(10))

# Gráfico para mostrar o desenvolvimento dos dados
q002Redacao = microdados_enem_selecionados.filter(items=['NU_NOTA_REDACAO', 'NO_Q002']).groupby('NO_Q002').mean().sort_values(by="NU_NOTA_REDACAO", ascending=False)
q002Redacao.plot()
plt.show()



