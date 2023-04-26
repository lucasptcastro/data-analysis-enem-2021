import pandas as pd

class DadosCandidatos:
    """Classe para coletar dados etários dos candidatos da edição 2021 do Enem."""
    
    def __init__(self, dataframe, limitador=0):
        self.df = pd.read_csv(dataframe, sep=";", encoding="ISO-8859-1") if limitador == 0 else pd.read_csv(dataframe, sep=";", encoding="ISO-8859-1")[0:limitador]

        self.colunas_dados_candidatos =['NU_INSCRICAO','TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_ESTADO_CIVIL', 'TP_COR_RACA', 'TP_NACIONALIDADE', 'TP_ST_CONCLUSAO', 'TP_ANO_CONCLUIU', 'TP_ESCOLA', 'TP_ENSINO', 'IN_TREINEIRO']

        self.df_candidatos = self.df.filter(items=self.colunas_dados_candidatos).dropna()

        self.dicionario_faixa_etaria = {
            1: "Menor de 17 anos",
            2: "17 anos",
            3: "18 anos",
            4: "19 anos",
            5: "20 anos",
            6: "21 anos",
            7: "22 anos",
            8: "23 anos",
            9: "24 anos",
            10: "25 anos",
            11: "Entre 26 e 30 anos",
            12: "Entre 31 e 35 anos",
            13: "Entre 36 e 40 anos",
            14: "Entre 41 e 45 anos",
            15: "Entre 46 e 50 anos",
            16: "Entre 51 e 55 anos",
            17: "Entre 56 e 60 anos",
            18: "Entre 61 e 65 anos",
            19: "Entre 66 e 70 anos",
            20: "Maior de 70 anos"
            }

    def retornar_faixas_etarias_candidatos(self):
        """Mostra o total de candidatos por faixa etária."""
        self.df_candidatos['DESCRICAO_FAIXA_ETARIA'] = [self.dicionario_faixa_etaria[item] for item in self.df_candidatos.TP_FAIXA_ETARIA]


        return self.df_candidatos.filter(items=['NU_INSCRICAO','DESCRICAO_FAIXA_ETARIA']).groupby('DESCRICAO_FAIXA_ETARIA').count().sort_values(by='NU_INSCRICAO', ascending=False)

















