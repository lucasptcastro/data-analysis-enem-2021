import pandas as pd
import matplotlib.pyplot as plt
from log.logger import Logger

classe_logger = Logger("DADOS-SOCIOECONOMICOS").get_logger()

class DadosSocioeconomicos:
    """Classe para coletar dados socioeconômicos dos candidatos da edição 2021 do Enem."""

    def __init__(self, dataframe, limitador=0) -> None:
        self.df = pd.read_csv(dataframe, sep=";", encoding="ISO-8859-1") if limitador == 0 else pd.read_csv(dataframe, sep=";", encoding="ISO-8859-1")[0:limitador]

        self.colunas_de_notas = ['NU_INSCRICAO', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'Q001', 'Q002']
        self.df_de_notas = self.df.filter(items=self.colunas_de_notas).dropna()

        # Q01 => Até que série seu pai, ou o homem responsável por você, estudou?
        # Q02 => Até que série sua mãe, ou a mulher responsável por você, estudou?
        self.dicionario_q001_e_q002 = {
            "A": "Nunca estudou",
            "B": "Não completou a 4ªsérie/5°ano do Ensino Fundamental",
            "C": "Completou a 4ªsérie/5°ano, mas não completou a 8ªsérie/9°ano do Ensino Fundamental",
            "D": "Completou a 8ªsérie/9°ano do Ensino Fundamental, mas não completou o Ensino Médio.",
            "E": "Completou o Ensino Médio, mas não completou a Faculdade.",
            "F": "Completou a Faculdade, mas não completou a Pós-Graduação.",
            "G": "Completou a Pós-Graduação.",
            "H": "Não sei."  
            }

    def retornar_dados_socioeconomicos_pais(self):
        """Mostra a contagem de dados socioeconômicos em relação a educação dos pais."""
        self.df_de_notas['NO_Q001'] = [self.dicionario_q001_e_q002[resp] for resp in self.df_de_notas.Q001] # Cria uma nova coluna contendo a descrição de cada valor da coluna Q001

        return self.df_de_notas.filter(items=['NU_INSCRICAO', 'NO_Q001']).groupby('NO_Q001').count().sort_values(by='NU_INSCRICAO', ascending=False)

    def retornar_dados_socioeconomicos_maes(self):
        """Mostra a contagem de dados socioeconômicos em relação a educação das mães."""
        self.df_de_notas['NO_Q002'] = [self.dicionario_q001_e_q002[resp] for resp in self.df_de_notas.Q002]

        return self.df_de_notas.filter(items=['NU_INSCRICAO', 'NO_Q002']).groupby('NO_Q002').count().sort_values(by='NU_INSCRICAO', ascending=False)

    def retornar_media_redacao_socioeconimica_pais(self):
        """Mostra a média de notas da redação em baseada na educação dos pais."""
        self.df_de_notas['NO_Q001'] = [self.dicionario_q001_e_q002[resp] for resp in self.df_de_notas.Q001]

        return self.df_de_notas.filter(items=['NU_NOTA_REDACAO', 'NO_Q001']).groupby('NO_Q001').mean().sort_values(by='NU_NOTA_REDACAO', ascending=False)

    def retornar_media_redacao_socioeconimica_maes(self):
        """Mostra a média de notas da redação em baseada na educação das mães."""
        self.df_de_notas['NO_Q002'] = [self.dicionario_q001_e_q002[resp] for resp in self.df_de_notas.Q002]

        return self.df_de_notas.filter(items=['NU_NOTA_REDACAO', 'NO_Q002']).groupby('NO_Q002').mean().sort_values(by="NU_NOTA_REDACAO", ascending=False)



