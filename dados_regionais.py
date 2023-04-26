import pandas as pd

class DadosRegionais:
    """Classe para coletar dados regionais dos candidatos da edição 2021 do Enem."""

    def __init__(self, dataframe, limitador=0) -> None:
        self.df = pd.read_csv(dataframe, sep=";", encoding="ISO-8859-1") if limitador == 0 else pd.read_csv(dataframe, sep=";", encoding="ISO-8859-1")[0:limitador]

        self.colunas_de_regioes =['NU_INSCRICAO', 'TP_NACIONALIDADE', 'CO_MUNICIPIO_PROVA', 'NO_MUNICIPIO_PROVA', 'CO_UF_PROVA', 'SG_UF_PROVA', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']
        self.df_regioes = self.df.filter(items=self.colunas_de_regioes).dropna()

    def retornar_numero_de_candidatos_por_estado(self):
        """Mostra a quantidade total de candidatos por cada estado em ordem decrescente."""

        return self.df_regioes.filter(items=['NU_INSCRICAO', 'SG_UF_PROVA']).groupby('SG_UF_PROVA').count().sort_values(by='NU_INSCRICAO', ascending=False)

    def retorna_media_notas_candidatos_por_estado(self):
        """Mostra a média disciplinar dos candidatos por cada estado."""

        return self.df_regioes.filter(items=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO', 'SG_UF_PROVA']).groupby('SG_UF_PROVA').mean().sort_values(by='NU_NOTA_REDACAO', ascending=False)




