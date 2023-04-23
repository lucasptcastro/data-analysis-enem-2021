import pandas as pd
import matplotlib.pyplot as plt
from log.logger import Logger
from analises import Analises

classe_logger = Logger("ANALISE").get_logger()
classe_analises = Analises('./dados/MICRODADOS_ENEM_2021_FORMATADO.csv', limitador=10000)

microdados_enem_formatado = classe_analises.df

colunas_selecionadas_enem = ['NU_INSCRICAO', 'NU_ANO', 'TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESTADO_CIVIL',
 'TP_COR_RACA', 'TP_NACIONALIDADE', 'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU',
 'TP_ESCOLA', 'TP_ENSINO', 'IN_TREINEIRO', 'CO_MUNICIPIO_ESC',
 'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC',
 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC', 'CO_MUNICIPIO_PROVA',
 'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'SG_UF_PROVA', 'TP_PRESENCA_CN',
 'TP_PRESENCA_CH', 'TP_PRESENCA_LC', 'TP_PRESENCA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']
df = microdados_enem_formatado.filter(items=colunas_selecionadas_enem) # Retorna um DF apenas com os valores das colunas passadas


# ===== TOTAL DE ALUNOS
coluna_inscricao = classe_analises.coletar_coluna("NU_INSCRICAO")
classe_logger.info(f'TOTAL DE INSCRIÇÕES ANALISADAS: {coluna_inscricao.count()}')


# ===== NOTA MÁXIMA CIÊNCIAS DA NATUREZA
coluna_ciencias_da_natureza = classe_analises.coletar_coluna("NU_NOTA_CN")
classe_logger.info(f'NOTA MÁXIMA PROVA DE CIÊNCIAS DA NATUREZA: {coluna_ciencias_da_natureza.max()} | MÉDIA: {coluna_ciencias_da_natureza.mean():.1f}')


# ===== NOTA MÁXIMA CIÊNCIAS HUMANAS
coluna_ciencias_humanas = classe_analises.coletar_coluna("NU_NOTA_CH")
classe_logger.info(f'NOTA MÁXIMA PROVA DE CIÊNCIAS HUMANAS: {coluna_ciencias_humanas.max()} | MÉDIA: {coluna_ciencias_humanas.mean():.1f}') 


# ===== NOTA MÁXIMA LINGUAGENS E CÓDIGOS
coluna_linguages_codigos = classe_analises.coletar_coluna("NU_NOTA_LC")
classe_logger.info(f'NOTA MÁXIMA PROVA DE LINGUAGENS E CÓDIGOS: {coluna_linguages_codigos.max()} | MÉDIA: {coluna_linguages_codigos.mean():.1f}') 


# ===== NOTA MÁXIMA MATEMÁTICA
coluna_matematica = classe_analises.coletar_coluna("NU_NOTA_MT")
classe_logger.info(f'NOTA MÁXIMA PROVA DE MATEMÁTICA: {coluna_matematica.max()} | MÉDIA: {coluna_matematica.mean():.1f}') 


# ===== MÉDIA DE NOTAS POR DISCIPLINA EM CADA ESTADO
linhas_estado_rn = df[(df["SG_UF_PROVA"] == "RN")]
print(f'MÉDIAS: {linhas_estado_rn["NU_NOTA_CN"].mean():.1f} {linhas_estado_rn["NU_NOTA_CH"].mean():.1f} {linhas_estado_rn["NU_NOTA_CH"].mean():.1f}')












































# ===== FAIXA ETARIA
coluna_faixa_etaria = classe_analises.coletar_coluna("TP_FAIXA_ETARIA")

fig_cfe, ax_cfe = plt.subplots(figsize=(8,5))

ax_cfe.hist(coluna_faixa_etaria, color="purple", bins=30)
ax_cfe.set_title('FAIXA ETARIA', fontsize=18)
ax_cfe.set_ylabel('VALORES', fontsize=14)
ax_cfe.set_xlabel('DESCRIÇÃO', fontsize=14)

# ===== ESTADOS DE APLICAÇÃO DA PROVA
coluna_sigla_estado_prova = classe_analises.coletar_coluna("SG_UF_PROVA")

fig_csep, ax_csep = plt.subplots(figsize=(8,5))

ax_csep.hist(coluna_sigla_estado_prova, color="orange", bins=27)
ax_csep.set_title('ESTADOS DE APLICAÇÃO DA PROVA', fontsize=18)
ax_csep.set_ylabel('VALORES', fontsize=14)
ax_csep.set_xlabel('UF', fontsize=14)

# ===== PERCENTUAL DE MULHERES GESTANTES 
coluna_sexo_candidatos = classe_analises.coletar_coluna("TP_SEXO")
total_sexo_feminino = coluna_sexo_candidatos.value_counts()[0]

total_sexo_feminino = classe_analises.coletar_valores("TP_SEXO")
# classe_logger.info(total_sexo_feminino)
# print(total_sexo_feminino)









# plt.show()